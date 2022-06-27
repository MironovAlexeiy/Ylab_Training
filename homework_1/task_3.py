def zeros(n) ->int:
    if n < 0:
        return 0
    else:
        res = 0
        while n > 0:
            n = int(n / 5)
            res += n

        return res


print(zeros(0))
print(zeros(5))
print(zeros(6))
print(zeros(11))
print(zeros(30))
print(zeros(100))
print(zeros(1000000000000000000))
