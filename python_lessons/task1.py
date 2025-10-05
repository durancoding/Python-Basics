"""
def square():
    ranged_numbers = range(1, 6)
    squared_numbers = [num ** 2 for num in ranged_numbers]
    return squared_numbers

print(square())

"""


def you_pay(cost, is_monday):
    if cost <= 50:
        cost = cost * 90/100
    elif 51 <= cost <= 100:
        if is_monday:
            cost = (cost - 10) * 80/100
        else:
            cost = cost * 80/100
    else:
        if is_monday:
            cost = (cost - 10) * 60/100
        else:
            cost = cost * 60/100
    return cost

print(you_pay(50, True))
print(you_pay(51, False))
print(you_pay(101, True))
print(you_pay(100, False))