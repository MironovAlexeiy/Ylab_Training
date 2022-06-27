from itertools import combinations


def bananas(s):
    result = set()
    name = 'banana'
    for combination in combinations(enumerate(s), 6):
        word = ['-' for i in range(len(s))]
        j = 0
        for i, letter in combination:
            if letter == name[j]:
                word[i] = letter
                j += 1
            else:
                break
        if j == len(name):
            result.add(''.join(word))
    return result

print(bananas("bbananana"))
print(bananas("banann"))
print(bananas("banana"))
print(bananas("bbananana"))
print(bananas("bananaaa"))
print(bananas("bananana"))
