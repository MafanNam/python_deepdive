import csv
from collections import namedtuple
from contextlib import contextmanager

f_names = 'data/cars.csv', 'data/personal_info.csv'

def get_dialect(f_name):
    with open(f_name) as f:
        return csv.Sniffer().sniff(f.read(1000))

class ContextManagerIter:
    def __init__(self, f_name):
        self.f_name = f_name

    def __enter__(self):
        self._f = open(self.f_name, 'r')
        self._reader = csv.reader(self._f, get_dialect(self.f_name))
        headers = map(lambda s: s.lower(), next(self._reader))
        self._nt = namedtuple('Data', headers)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration
        return self._nt(*next(self._reader))


# with ContextManagerIter('data/cars.csv') as f:
#     for row in f:
#         print(row)



def parsed_data_iter(data_iter, nt):
    for row in data_iter:
        yield nt(*row)


@contextmanager
def parsed_data(f_name):
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(1000))
        f.seek(0)
        reader = csv.reader(f, dialect)
        headers = map(lambda s: s.lower(), next(reader))
        nt = namedtuple('Data', headers)
        yield (nt(*row) for row in reader)
    finally:
        f.close()


with parsed_data(f_names[-1]) as f:
    for row in f:
        print(row)






