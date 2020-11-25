def fastPower(base, power):
    result = 1
    while power > 0:
        if power % 2 == 0:
            power = power / 2
            base = base * base
        else:
            power = (power - 1) / 2
            result = result * base
            base = base * base
    return result      