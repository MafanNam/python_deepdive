from datetime import datetime
from collections import namedtuple
import csv


def csv_parser(file_name, *, delimiter=',', quotechar='"', include_header=False):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        if not include_header:
            next(f)
        yield from reader


def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)


def extract_field_names(name):
    reader = csv_parser(name, include_header=True)
    return next(reader)


def create_named_tuple_class(name, class_name):
    fields = extract_field_names(name)
    return namedtuple(class_name, fields)


def iter_file(name, class_name, parser):
    nt_class = create_named_tuple_class(name, class_name)
    reader = csv_parser(name)

    for row in reader:
        parsed_data = (parse_fn(value) for value, parse_fn in zip(row, parser))
        yield nt_class(*parsed_data)


