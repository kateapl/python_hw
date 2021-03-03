def check_power_of_2(a: int) -> bool:
    i = 1
    while i < a:
        i = i * 2
        if i == a:
            return True
    return False
