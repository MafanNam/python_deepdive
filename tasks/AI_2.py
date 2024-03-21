import tkinter as tk
from tkinter import messagebox
import random

from PIL.ImageTk import PhotoImage

zodiac_descriptions = {
    "Овен": "Люди, народжені під знаком Овна, зазвичай відзначаються своєю енергією, наполегливістю та рішучістю. Вони часто бувають лідерами, які йдуть вперед і відчувають себе комфортно у ролі піонерів. Овни відомі своєю впертістю та схильністю до амбіційних проектів.",
    "Телець": "Телець - це знак стійкості та надійності. Люди, що народилися під цим знаком, зазвичай відзначаються своєю стабільністю та терплячістю. Вони цінують комфорт та матеріальні блага, а також можуть бути дуже пристрасними у своїх уподобаннях.",
    "Близнята": "Близнята - це знак комунікативності та адаптивності. Люди, що народилися під цим знаком, зазвичай відзначаються своєю розумністю та жвавістю. Вони можуть бути дуже допитливими та цікавитися різними аспектами життя.",
    "Рак": "Раки - це знак чутливості та емоційності. Люди, що народилися під цим знаком, зазвичай відзначаються своєю здатністю до співчуття та відданістю. Вони можуть бути дуже захисницькими щодо своїх близьких та сім'ї.",
    "Лев": "Леви - це знак впевненості та гордості. Люди, що народилися під цим знаком, зазвичай відзначаються своєю харизмою та лідерськими якостями. Вони можуть бути дуже впертими та вимогливими, але також великодушними та щедрими.",
    "Діва": "Діви - це знак аналітичності та практичності. Люди, що народилися під цим знаком, зазвичай відзначаються своєю організованістю та дотепністю. Вони можуть бути дуже критичними, як до себе, так і до інших, але завдяки цьому часто досягають успіху у своїх справах.",
    "Терези": "Терези - це знак справжніх партнерів та вірних друзів. Люди, що народилися під цим знаком, зазвичай відзначаються своєю співчутливістю та спокоєм. Вони можуть бути дуже рішучими та міцними, коли потрібно захистити своїх близьких.",
    "Скорпіон": "Скорпіони - це знак страсті та влади. Люди, що народилися під цим знаком, зазвичай відзначаються своєю наполегливістю та визначністю. Вони можуть бути дуже пристрасними та інтенсивними у своїх відносинах та діях.",
    "Стрілець": "Стрільці - це знак пригодництва та оптимізму. Люди, що народилися під цим знаком, зазвичай відзначаються своєю ентузіазмом та енергією. Вони можуть бути дуже відкритими та прямодушними, а також цінують свободу та незалежність.",
    "Козеріг": "Козероги - це знак практичності та амбіційності. Люди, що народилися під цим знаком, зазвичай відзначаються своєю цілеспрямованістю та відповідальністю. Вони можуть бути дуже наполегливими та мають сильний бажання досягати своїх цілей. Козероги цінують традиції та стабільність і часто проявляють консервативний підхід до життя.",
    "Водолій": "Водолії - це знак оригінальності та інноваційності. Люди, що народилися під цим знаком, зазвичай відзначаються своєю незалежністю та прогресивним мисленням. Вони можуть бути дуже ексцентричними та експериментальними у своїх ідеях та діях.",
    "Риби": "Риби - це знак чутливості та інтуїції. Люди, що народилися під цим знаком, зазвичай відзначаються своєю емпатією та сприйнятливістю до енергій навколишнього світу. Вони можуть бути дуже творчими та мрійливими, а також віддані своїм ідеалам і вірують у духовні цінності.",
}

horoscope_options = ["На день", "На тиждень", "На місяць"]


def generate_daily_horoscope(sign):
    return f"Сьогодні для {sign}: {random.choice(['гарний день для нових початків.', 'зустріньте несподіваного друга.', 'будьте обережні в угодах.'])}"


def generate_weekly_horoscope(sign):
    return f"На цей тиждень для {sign}: {random.choice(['дізнаєтеся цікаву інформацію.', 'очікується подорож або цікаві знайомства.', 'будьте вдумливими у прийнятті рішень.'])}"


def generate_monthly_horoscope(sign):
    return f"На цей місяць для {sign}: {random.choice(['здійсниться ваша давня мрія.', 'займайтеся спортом для покращення енергії.', 'будьте готові до змін в особистому житті.'])}"


def show_horoscope():
    selected_sign = zodiac_combobox.get()
    selected_horoscope = horoscope_combobox.get()

    description = zodiac_descriptions.get(selected_sign, "Опис недоступний")

    if selected_horoscope == "На день":
        horoscope_text = generate_daily_horoscope(selected_sign)
    elif selected_horoscope == "На тиждень":
        horoscope_text = generate_weekly_horoscope(selected_sign)
    elif selected_horoscope == "На місяць":
        horoscope_text = generate_monthly_horoscope(selected_sign)
    else:
        horoscope_text = "Гороскоп недоступний"

    messagebox.showinfo(selected_sign, f"{description}\n\n{horoscope_text}")


root = tk.Tk()
root.title("Прогноз за знаком зодіаку")
# root.configure(padx="100", pady="100")


# Завантаження фонового зображення
background_image = PhotoImage(file="hoodie-cute-anime-girl-09.jpg")
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry("500x500")
bg = PhotoImage(file="bd_horoscope.png")

canvas1 = tk.Canvas(root, width=500, height=500)
canvas1.pack(fill="both", expand=True)

canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

# Кольори та стиль
zodiac_label = tk.Label(root, text="Виберіть свій знак зодіаку:", bg="#bc3ef0", fg="#fbf8ff", font=("Helvetica", 12))
canvas1.create_window(160, 50, anchor="nw", window=zodiac_label)

zodiac_combobox = tk.StringVar()
zodiac_combobox.set("Овен")  # Значення за замовчуванням

zodiac_menu = tk.OptionMenu(root, zodiac_combobox, *zodiac_descriptions.keys())
zodiac_menu.config(bg="#4d4ad3", font=("Helvetica", 10))
# zodiac_menu.pack()
canvas1.create_window(213, 100, anchor="nw", window=zodiac_menu)

horoscope_label = tk.Label(root, text="Оберіть період гороскопу:", bg="#bc3ef0", fg="#fbf8ff", font=("Helvetica", 12))
# horoscope_label.pack()
canvas1.create_window(160, 150, anchor="nw", window=horoscope_label)

horoscope_combobox = tk.StringVar()
horoscope_combobox.set("На день")  # Значення за замовчуванням
horoscope_menu = tk.OptionMenu(root, horoscope_combobox, *horoscope_options)
horoscope_menu.config(bg="#4d4ad3", font=("Helvetica", 10))
# horoscope_menu.pack()
canvas1.create_window(200, 200, anchor="nw", window=horoscope_menu)

show_button = tk.Button(root, text="Показати гороскоп", command=show_horoscope, bg="#008CBA", fg="white",
                        font=("Helvetica", 12))
# show_button.pack()
canvas1.create_window(175, 300, anchor="nw", window=show_button)

root.mainloop()
