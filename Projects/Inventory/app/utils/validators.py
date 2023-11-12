def validate_integer(
        arg_name: str, arg_value: object, min_value: int = None, max_value: int = None,
        custom_min_message: str = None, custom_max_message: str = None,
) -> None:
    if not isinstance(arg_value, int):
        raise TypeError(f"{arg_name} must be an integer.")

    if min_value is not None and arg_value < min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f"{arg_name} cannot be less then {min_value}")

    if max_value is not None and arg_value > max_value:
        if custom_max_message is not None:
            raise ValueError(custom_max_message)
        raise ValueError(f"{arg_name} cannot be less then {max_value}")
