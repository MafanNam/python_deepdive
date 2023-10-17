import datetime
import itertools

import constants
import parse_utils


# for name, class_name, parser in zip(constants.names, constants.class_names, constants.parsers):
#     file_iter = parse_utils.iter_file(name, class_name, parser)
#     print(name)
#     for _ in range(3):
#         print(next(file_iter))

# gen = parse_utils.iter_combined_plain_tuple(constants.names, constants.class_names,
#                                             constants.parsers, constants.compress_fields)
#
# print(list(next(gen)))
# print(list(next(gen)))


# nt = parse_utils.create_combo_named_tuple_class(constants.names, constants.compress_fields)
# print(nt._fields)

# data_iter = parse_utils.iter_combined(constants.names, constants.class_names,
#                                       constants.parsers, constants.compress_fields)
#
# for row in itertools.islice(data_iter, 5):
#     print(row)


def group_key(item):
    return item.gender, item.vehicle_make


# data = parse_utils.filtered_iter_combined(constants.names, constants.class_names,
#                                           constants.parsers, constants.compress_fields)

# for row in itertools.islice(data_iter, 5):
#     print(row)
#
# sorted_data = sorted(data, key=group_key)
#
# groups_1 = itertools.groupby(sorted_data, key=group_key)
# groups_2 = itertools.groupby(sorted_data, key=group_key)
#
# group_f = (item for item in groups_1 if item[0][0 == 'Female'])
# data_f = ((item[0][1], len(list(item[1]))) for item in group_f)
#
#
# group_m = (item for item in groups_2 if item[0][0 == 'Male'])
# data_m = ((item[0][1], len(list(item[1]))) for item in group_m)
#
#
# for row in data_f:
#     print(row)
#
# for row in data_m:
#     print(row)

# data_1, data_2 = itertools.tee(data, 2)
#
# data_m = (row for row in data_1 if row.gender == 'Male')
# sorted_data_m = sorted(data_m, key=group_key)
# groups_m = itertools.groupby(sorted_data_m, key=group_key)
#
# data_f = (row for row in data_2 if row.gender == 'Female')
# sorted_data_f = sorted(data_f, key=group_key)
# groups_f = itertools.groupby(sorted_data_f, key=group_key)
#
# for row in groups_m:
#     print(row)
#
# for row in groups_f:
#     print(row)

cutoff_data = datetime.datetime(2017, 3, 1)

results_f = parse_utils.group_data(constants.names, constants.class_names,
                                   constants.parsers, constants.compress_fields,
                                   filter_key=lambda row: row.last_updated >= cutoff_data,
                                   group_key=lambda row: row.vehicle_make,
                                   gender='Female')

results_m = parse_utils.group_data(constants.names, constants.class_names,
                                   constants.parsers, constants.compress_fields,
                                   filter_key=lambda row: row.last_updated >= cutoff_data,
                                   group_key=lambda row: row.vehicle_make,
                                   gender='Male')
for row in results_f:
    print(row)

for row in results_m:
    print(row)
