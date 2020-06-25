def sqrt(a):
    a_type = type(a)
    if a_type == int:
        if a > 0:
            return a ** 0.5
        else:
            raise ValueError(f'Negative integer passed: {a}')
    elif a_type == str:
        if a.isnumeric():
            return int(a) ** 0.5
        else:
            raise ValueError(f'Not a numeric string passed: {a}')
    else:
        raise ValueError(f'Unsuported type passed: {a_type}')
