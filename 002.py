"""
Даны два целых числа A и В (каждое в отдельной строке). Выведите все числа от A до B включительно,
в порядке возрастания, если A < B, или в порядке убывания в противном случае.

Ввод	Вывод
5 1      5 4 3 2 1
"""
def recursion(a, b):

    if a == b:
        return b

    if a < b:
        return a , recursion(a + 1, b)

    if a > b:
        return a, recursion(a - 1, b)


print(recursion(1, 5))

print(recursion(5, 1))
