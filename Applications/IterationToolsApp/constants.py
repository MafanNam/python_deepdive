from parse_utils import parse_date

# Files
name_personal = './data/personal_info.csv'
name_employment = './data/employment.csv'
name_vehicles = './data/vehicles.csv'
name_update_status = './data/update_status.csv'

names = name_personal, name_employment, name_vehicles, name_update_status

# Parents
personal_parser = (str, str, str, str, str)
employment_parser = (str, str, str, str)
vehicles_parser = (str, str, str, int)
update_status_parser = (str, parse_date, parse_date)

parsers = personal_parser, employment_parser, vehicles_parser, update_status_parser

# Named Tuple Names
personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'

class_names = personal_class_name, employment_class_name, vehicle_class_name, update_status_class_name

# Field Inclusion/Exclusion
personal_fields_compress = [True, True, True, True, True]
employment_fields_compress = [True, True, True, False]
vehicle_fields_compress = [False, True, True, True]
update_status_fields_compress = [False, True, True]
compress_fields = (personal_fields_compress, employment_fields_compress,
                   vehicle_fields_compress, update_status_fields_compress)
