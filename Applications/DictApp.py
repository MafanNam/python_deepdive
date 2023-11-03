john = {
    'user_id': 100,
    'name': {
        'first': 'fff',
        'last': 'dsfsd',
    },
    'bio': {
        'dob': {
            'year': 1934,
            'month': 11,
            'day': 34,
        },
        'birthplace': {
            'country': 'rerwr',
            'city': 'refrefergfe',
        }
    }
}

eric = {
    'user_id': 101,
    'name': {
        'first': 'effe3',
        'last': 'ergfeg',
    },
    'bio': {
        'dob': {
            'year': 123,
            'month': 4,
            'day': 55,
        },
        'birthplace': {
            'country': 'erffer',
            # 'city': str,
        }
    }
}

maxi = {
    'user_id': 102,
    'name': {
        'first': 'erger',
        'last': 'ergreg',
    },
    'bio': {
        'dob': {
            'year': 1932,
            'month': 'May',    # error type
            'day': 5,
        },
        'birthplace': {
            'country': 'fdsf',
            'city': 'sdfsf',
        }
    }
}



template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str,
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int,
        },
        'birthplace': {
            'country': str,
            'city': str,
        }
    }
}

def key_pic(d: dict) -> set:
    keys = set()
    for k, v in d.items():
        keys.add(k)
        if type(v) == dict:
            for k2, v2 in v.items():
                keys.add(k2)
                if type(v2) == dict:
                    for k3, v3 in v2.items():
                        keys.add(k3)
    return keys


def value_detect_type(d: dict) -> dict:
    for k, v in d.items():
        if type(v) != dict:
            d[k] = type(v)
        else:
            for k2, v2 in v.items():
                if type(v2) != dict:
                    d[k][k2] = type(v2)
                else:
                    for k3, v3 in v2.items():
                        if type(v3) != dict:
                            d[k][k2][k3] = type(v3)
    return d

# print(value_detect_type(eric))

# print(key_pic(template))
# print(key_pic(eric))


def validate(data: dict, template: dict):
    data_keys = key_pic(data)
    template_keys = key_pic(template)

    if data_keys != template_keys:
        return False, f"miss key(s): {template_keys - data_keys}"

    data_val = value_detect_type(data)

    if data_val != template:
        return False, "error type"

    return True









print(validate(john, template)) # True
print(validate(eric, template)) # False, miss key
print(validate(maxi, template)) # False, type error














