from collections import namedtuple
from datetime import datetime

with open('data/nyc_parking_tickets_extract.csv') as f:
    column_headers = next(f).strip().split(',')
    data = (i.strip().split(',') for i in f)

column_names = [header.replace(' ', '_').lower() for header in column_headers]
Ticket = namedtuple('Ticket', column_names)


def read_data():
    with open('data/nyc_parking_tickets_extract.csv') as f:
        next(f)
        yield from f


def parse_int(value: int, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_string(value: str, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default


column_parsers = (parse_int,
                  parse_string,
                  lambda x: parse_string(x, default=''),
                  lambda x: parse_string(x, default=''),
                  parse_date,
                  parse_int,
                  lambda x: parse_string(x, default=''),
                  parse_string,
                  lambda x: parse_string(x, default=''),
                  )


def parse_row(row, *, default=None):
    fields = row.strip().split(',')
    parsed_data = [funk(field) for funk, field in zip(column_parsers, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    return default


# rows = read_data()
#
# for _ in range(5):
#     row = next(rows)
#     parsed_data = parse_row(row)
#     print(parsed_data)


# for row in read_data():
#     parsed_row = parse_row(row)
#     if parsed_row is None:
#         print(list(zip(column_names, row.strip().split(','))),
#               end='\n\n')


def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed


# parsed_rows = parsed_data()
#
# for _ in range(5):
#     print(next(parsed_rows))


##########################################

def violation_count_by_make():
    makes_counts = {}

    for data in parsed_data():
        if data.vehicle_make in makes_counts:
            makes_counts[data.vehicle_make] += 1
        else:
            makes_counts[data.vehicle_make] = 1

    return dict(sorted(makes_counts.items(), key=lambda t: (t[1], t[0])))


violation = violation_count_by_make()

print(violation)
