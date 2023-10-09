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


data_iter = parse_utils.filtered_iter_combined(constants.names, constants.class_names,
                                               constants.parsers, constants.compress_fields,
                                               key=lambda row: row.ssn == '104-84-7144')

for row in itertools.islice(data_iter, 5):
    print(row)
