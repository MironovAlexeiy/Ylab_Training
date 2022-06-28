"""
В втором тесте:
primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]
Самое большое число должно быть меньше предела по условию
"""
from functools import reduce
from operator import mul


def count_find_num(primesL, limit):
    if reduce(mul, primesL) > limit:
        return []
    else:
        multiplication_primesL = reduce(mul, primesL)
        result = []
        result.append(multiplication_primesL)
        for num in primesL:
            for m in result:
                mult = num * m
                while mult <= limit and mult not in result:
                    result.append(mult)
                    mult *= num
        return [len(result), max(result)]


print(count_find_num([2, 5, 7], 500))
print(count_find_num([2, 3], 200))
print(count_find_num([2, 5], 200))
print(count_find_num([2, 3, 5], 500))
print(count_find_num([2, 3, 5], 1000))
print(count_find_num([2, 3, 47], 200))
