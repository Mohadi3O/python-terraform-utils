def get_class_name(name: str) -> str:
    return snake_case_to_pascal_case(name)


def snake_case_to_pascal_case(string: str) -> str:
    return ''.join(map(lambda s: s.title(), string.split('_')))
