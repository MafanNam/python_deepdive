import constants
import parse_utils

for name, class_name, parser in zip(constants.names, constants.class_names, constants.parsers):
    file_iter = parse_utils.iter_file(name, class_name, parser)
    print(name)
    for _ in range(3):
        print(next(file_iter))
