"""
Написать программу, принимающую на вход 2 дроби (вида a/b) (знаменатель одинаковый)
и выводящую результат сложения дробей “a/b + c/b = x/b”​
​
Пример: a/b = 1/3 c/b = 5/3 ​
Вывод: 1/3 + 5/3 = 6/3
"""

n = str(input())
a = n.split("/")[0]
b = n.split("/")[1]
m = str(input())
c = m.split("/")[0]

d = int(a) + int(c)

print(f"{n} + {m} = {d}/{b}")

"""
a_b = input().split('/')
c_b = input().split('/')

a, b = int(a_b[0]), int(a_b[1])
c, b = int(c_b[0]), int(c_b[1])

print(f'{a}/{b} + {c}/{b} = {a+c}/{b}')
"""