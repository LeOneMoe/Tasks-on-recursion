"""
Дано натуральное число n. Выведите все числа от 1 до n.

Ввод	Вывод
5       1 2 3 4 5
"""
def recursion(n):
    if n == 0:
        return n

    if n == 1:
        return n

    return recursion(n - 1) , n

print(recursion(5))
