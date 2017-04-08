"""
Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.

Операцией возведения в степень пользоваться нельзя!

Ввод	Вывод
8       YES

3       NO
"""
def recursion(n, powtwo=1):
    if n == 1:
        return "YES"

    if powtwo == n:
        return "YES"

    if powtwo > n:
        return "NO"

    if powtwo < n:
        return recursion(n, powtwo * 2)


for n in range(100):
    print("%i - " % n, recursion(n))
