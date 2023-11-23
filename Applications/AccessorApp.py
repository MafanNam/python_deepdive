DB = {
    'Person': {
        1: {'first_name': 'Isaac', 'last_name': 'Newton', 'born': 1642, 'country_id': 1},
        2: {'first_name': 'Gottfried', 'last_name': 'von Leibniz', 'born': 1646, 'country_id': 5},
        3: {'first_name': 'Joseph', 'last_name': 'Fourier', 'born': 1768, 'country_id': 3},
        4: {'first_name': 'Bernhard', 'last_name': 'Riemann', 'born': 1826, 'country_id': 5},
        5: {'first_name': 'David', 'last_name': 'Hilbert', 'born': 1862, 'country_id': 5},
        6: {'first_name': 'Srinivasa', 'last_name': 'Ramanujan', 'born': 1887, 'country_id': 4},
        7: {'first_name': 'John', 'last_name': 'von Neumann', 'born': 1903, 'country_id': 2},
        8: {'first_name': 'Andrew', 'last_name': 'Wiles', 'born': 1928, 'country_id': 6}
    },
    'Country': {
        1: {'name': 'United Kingdom', 'capital': 'London', 'continent': 'Europe'},
        2: {'name': 'Hungary', 'capital': 'Budapest', 'continent': 'Europe'},
        3: {'name': 'France', 'capital': 'Paris', 'continent': 'Europe'},
        4: {'name': 'India', 'capital': 'New Delhi', 'continent': 'Asia'},
        5: {'name': 'Germany', 'capital': 'Berlin', 'continent': 'Europe'},
        6: {'name': 'USA', 'capital': 'Washington DC', 'continent': 'North America'}
    }
}


# class Country:
#     def __init__(self, id_):
#         if id_ in DB['Country']:
#             self._db_record = DB['Country'][id_]
#         else:
#             raise ValueError(f'Record not found (Country.id={id_})')
#
#     @property
#     def name(self):
#         return self._db_record['name']
#
#     @property
#     def capital(self):
#         return self._db_record['capital']
#
#     @property
#     def continent(self):
#         return self._db_record['continent']


class DBRecord:
    def __init__(self, db_record_dict):
        super().__setattr__('_record', db_record_dict)

    def __getattr__(self, item):
        record = super().__getattribute__('_record')
        if record and item in record:
            return record[item]
        raise AttributeError(f"Field name '{item}' does not exist.")

    def __setattr__(self, key, value):
        record = super().__getattribute__('_record')
        if record and key in record:
            record[key] = value
        raise AttributeError(f"Field name '{key}' does not exist.")

    @property
    def fields(self):
        record = super().__getattribute__('_record')
        return tuple(record.keys())


class DBTable:
    def __init__(self, db, table_name):
        if table_name not in db:
            raise ValueError(f"The table {table_name} does not exist in the database.")
        self._table_name = table_name
        self._table = db[table_name]

    @property
    def table_name(self):
        return self._table_name

    def __call__(self, record_id):
        if record_id not in self._table:
            raise ValueError(f"Specified id ({record_id}) does not exist.")
        return DBRecord(self._table[record_id])


tbl_person = DBTable(DB, 'Person')
tbl_country = DBTable(DB, 'Country')

p1 = tbl_person(1)
print(p1.country_id)
# print(p1.__dict__)

country_1 = tbl_country(p1.country_id)
print(country_1.name, country_1.capital, country_1.continent)

print(p1.fields)
