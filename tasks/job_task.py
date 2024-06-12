# ---------------------------------------------------------------------------------------------------------------

# 1 [Розробка] Фільтрування великої таблиці за даними з повʼязаної таблиці та сортування

class Product(Model):
    class Meta:
        db_table = "product"
        index_together = [["category_id", "price"], ["category_id", "rank"]]

    name = models.TextField(_("Name"))
    category = models.ForeignKey(
        Category, RESTRICT, verbose_name=_("Category"), related_name="products")
    price = models.DecimalField(_("Price"), decimal_places=2, max_digits=10, null=True)
    rank = models.DecimalField(_("Price"), decimal_places=2, max_digits=10, null=True)
    perks = models.ManyToManyField(Perk, verbose_name=_("Perks"), related_name="products")


# ...

class Category(Model):
    class Meta:
        db_table = "category"

    name = models.TextField(_("Name"), unique=True)


# ...

class Perk(Model):
    class Meta:
        db_table = "perk"

    name = models.TextField(_("Name"), unique=True)


# РОЗДУМИ
# Так як у нас дуже багато фільтрацій та товарів також відносно багато, потрібно оптимізовувати запити до бази даних.

# Реалізація
# 1. Використання ідексів
# В коді вже використовуються індеки category_id, price та rank, я б довавив індексацію ще price.
# Проте index_together застаріле, на нових версіях слід використовувати indexes.

class Product(Model):
    class Meta:
        db_table = "product"
        indexes = [
            models.Index(fields=['price']),
            models.Index(fields=['category_id', 'price']),
            models.Index(fields=['category_id', 'rank']),
        ]

    name = models.TextField(_("Name"))
    category = models.ForeignKey(
        Category, RESTRICT, verbose_name=_("Category"), related_name="products")
    price = models.DecimalField(_("Price"), decimal_places=2, max_digits=10, null=True)
    rank = models.DecimalField(_("Price"), decimal_places=2, max_digits=10, null=True)
    perks = models.ManyToManyField(Perk, verbose_name=_("Perks"), related_name="products")


# 2. Оптимізація запитів за допомогою select_related та prefetch_related
# При фільтрації(вибірці) ми отримаємо інформацію з пов'язаних таблиць, і буде проблема 1+N, дублікація не потрібних запитів.
# При велицій кількості данних це суттєво розгрузить нашу бд.

# view.py
class ListProductAPIView(generic.ListAPIView):
    """Public API endpoint for listing products."""

    def get_queryset(self):
        return Product.objects.select_related("category").prefetch_related("perks")


# Тут ми вибірку по категоріям запизнуви в головний запит, а перкі в згруповали в ще один запит


# 3.Оптимізація фільтрів
# Я б фільтрував запити поступово і за необхідністю, використовуючи проміжні результати.
# Реалізація "це одне зі значень зі списку: [0, 100, 500, 1000, 2000, 5000, 10000, 25000, 100000]" має бути не у фільтрацї.

def filter_products(category_id, price_from=None, price_to=None, perk_id_list=None):
    products = Product.objects.filter(category_id=category_id)

    if price_min is not None:
        products = products.filter(price__gte=price_min)

    if price_max is not None:
        products = products.filter(price__lte=price_max)

    if perk_id_list:
        products = products.filter(perks__id__in=perk_id_list).distinct()

    return products


# Це псевдо код для розуміння, що потрібно розділяти запит фільтрації на етапи а не все за раз.
# Так то для фільтрації слід використовувати django-filters, або ще якісь пакети для фільтрації.


# 4. Дотаток
# можна встановити-налаштувати пакет django-debug-toolbar,
# і там вже детальніше розглянути вибірки(наприклад щоб кешувати сильно затратні запити).
# Якщо цього не достатньо, можна зменшити пагінацію обєктів тобто objects page замість 30 зробити 25, 20.

# ---------------------------------------------------------------------------------------------------------------

# 2.[Development] Save data from the JSON

class Status(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    PAUSED = "PAUSED", "Paused"
    DELETED = "DELETED", "Deleted"
    ARCHIVED = "ARCHIVED", "Archived"


class AdCreative(models.Model):  # image for ad
    fb_id = models.TextField("Unique Identifier", unique=True)
    created_at = models.DateTimeField("Fb Creation Date")
    title = models.TextField("Title")
    description = models.TextField("Description", null=True, blank=True)
    url = models.URLField("Image url")

    class Meta:
        db_table = "ad_creative"


class AdCampaign(models.Model):  # advertising campaign
    fb_id = models.TextField("Unique Identifier", unique=True)
    created_at = models.DateTimeField("Fb Creation Date")
    name = models.TextField("Name")
    status = models.TextField("Status", choices=Status.choice)
    description = models.TextField("Description")
    budget = models.DecimalField("Budget", decimal_places=2, max_digits=10)

    class Meta:
        db_table = "ad_campaign"


class Adset(models.Model):  # group of ads for ad campaign
    ad_campaign = models.ForeignKey(AdCampaign, on_delete=models.CASCADE)
    fb_id = models.TextField("Unique Identifier", unique=True)
    created_at = models.DateTimeField("Fb Creation Date")
    name = models.TextField("Name")
    status = models.TextField("Status", choices=Status.choice)
    description = models.TextField("Description")
    budget = models.DecimalField("Budget", decimal_places=2, max_digits=10)

    class Meta:
        db_table = "adset"


class Ad(models.Model):
    ad_campaign = models.ForeignKey(AdCampaign, on_delete=models.CASCADE)
    adset = models.ForeignKey(Adset, on_delete=models.CASCADE)
    fb_id = models.TextField("Unique Identifier", unique=True)
    created_at = models.DateTimeField("Fb Creation Date")
    name = models.TextField("Name")
    status = models.TextField("Status", choices=Status.choice)
    active_ad_creative = models.ForeignKey(AdCreative, on_delete=models.CASCADE)

    class Meta:
        db_table = "ad"


# -------------------------
# Реалізація

class AdCreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdCreative
        fields = ['fb_id', 'title', 'description', 'created_at', 'url']


class AdSerializer(serializers.ModelSerializer):
    active_ad_creative = serializers.CharField(source='active_ad_creative.fb_id', read_only=True)

    class Meta:
        model = Ad
        fields = ['fb_id', 'name', 'status', 'created_at', 'active_ad_creative']


class AdsetSerializer(serializers.ModelSerializer):
    ad_list = AdSerializer(many=True)

    class Meta:
        model = Adset
        fields = ['fb_id', 'name', 'status', 'description', 'budget', 'created_at', 'ad_list']


class AdCampaignSerializer(serializers.ModelSerializer):
    adset_list = AdsetSerializer(many=True)

    class Meta:
        model = AdCampaign
        fields = ['fb_id', 'name', 'status', 'description', 'budget', 'created_at', 'adset_list']

    def update(self, instance, validated_data):

        logger.debug(f"Updating AdCampaign {instance.fb_id}")

        # Update AdCampaign instance
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.budget = validated_data.get('budget', instance.budget)

        # Update Adset instances
        for adset_data in validated_data.get('adset_list', []):
            adset_id = adset_data.get('fb_id')
            try:
                adset_instance = instance.adset_list.get(fb_id=adset_id)
            except Adset.DoesNotExist:
                logger.error(f"Adset with fb_id '{adset_id}' does not exist")

                raise ValidationError(f"Adset with fb_id '{adset_id}' does not exist")

            logger.debug(f"Updating Adset {adset_id}")
            adset_instance.name = adset_data.get('name', adset_instance.name)
            # ...
            adset_instance.save()

            # Update Ad instances
            for ad_data in adset_data.get('ad_list', []):
                # Тут все дуже схоже
                pass

        instance.save()
        return instance


class MainSerializer(serializers.Serializer):
    ad_campaign = AdCampaignSerializer()
    ad_creative = AdCreativeSerializer(many=True)


# І так, в MainSerializer реалізовано сукупність двох серіалізаторів.
# Далі, відбувається об'єднання обох серіалізаторів в один.
# Насравді тут в AdCampaignSerializer трьохрівнева вкладеність я б реалізовува це через пакет щось типу django-nested-serializers.
# Поле active_ad_creative я реалізував за CharFiled(source='active_ad_creative.fb_id', read_only=True), по прикладу який ви прикріпили.
# Також була додана перевірка на валідність даних, та більш менш правильне їх оновлення і збереження.
# Просте логування під час роботи серіалізатора реалізоване в функції update.
# Я не тестував реалізацію(недостатньо часу), тому не впевнений, що серіалізатор повністю відповідає вимогам.

# ---------------------------------------------------------------------------------------------------------------

# 3. [Design] How to implement i18n for a few similar models with flexible management opportunities?

# З того що я зрозумів при розробці схеми бази даних (БД) для вашого веб-сайту вам потрібно врахувати всі вимоги та обмеження.
# + ще потрібна підтримка різних мов та локалізація.
# Легке керування та щоб можна було легко розширяти пул нових мов.

# Ця задача точно не на декілька годин, тому все буде абстрактно.

# Мої роздуми:
# Для початку потрібна певна схема бази даних з сутностями.

# Сутності та їх відношення:
#     Курс: Це основна сутність, яка містить інформацію про кожен курс.
#     Навички: Кожен курс може мати декілька навичок, пов'язаних з ним.
#     Професія: Курс може бути пов'язаний з певною професією.
#     Галузь: Кожна професія може бути пов'язана з певною галуззю.
#
# Таблиці в базі даних:
#     Course: Поля цієї таблиці можуть включати інформацію, таку як ID курсу, назва курсу, опис, мови навчання тощо.
#     Skills: Тут ви можете мати поля, що вказують на ID курсу та назву навички.
#     Profession: Можливо, знадобиться таблиця, де будуть зберігатися дані про професії, їх опис і ID галузі.
#     Industry: Тут ви можете мати таблицю з назвою галузі та її описом.
#
#  валідація:
#     Кожна сутність має бути взаємоповязаною з іншими сутностями через зовнішні ключі.
#     Валідація введення даних може бути здійснювана на рівні веб застосунку та БД.
#
# Пошук за назвою:
#    Для забезпечення пошуку за назвою кожної сутності як я вже уточнював в першому завданні можна використовувати індексацію відповідних полів у БД.
#
# Мультимовна підтримка:
#     Можна мати окремі поля для кожної мови, де зберігатимете переклади текстів(не краща реалізація).
#     Можна використовувати AI для перекладу текстів і зберігати переклади в БД, тобто з такою реалізацією буде дуже просто та комфортно працювати та маштабувати.
#     Зберігати дані у JSON-форматі для кожної мови, я точно не памятаю як це називається типу якогось мовного словника.

# Що до переводу, мені здається що вже є якісь готові реалізації цього типу пакетів,
# але найкращою ідеєю було би використовувати інструменти AI.

class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ...


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    languages = models.ManyToManyField(_("Language"), Language, related_name="courses")
    ...


class Skill(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    ...


class Profession(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name="professions")
    ...


class Industry(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ...

# Це якщо супер спростити


# На цьому все, дякую за цікаві завдання :)


