def check_power_of_2(a: int) -> bool:
    return not a & (a - 1)