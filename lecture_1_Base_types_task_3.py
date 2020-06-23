"""
Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить
слово Fizz, а вместо чисел, кратных пяти — слово Buzz.
Если число кратно и 3, и 5, то программа должна выводить слово FizzBuzz.
"""


def fizzbuzz(args):
    arr = []
    for i in args:
        temp = ''
        if i % 3 == 0:
            temp = 'Fizz'
        if i % 5 == 0:
            temp = 'Buzz'
        if i % 15 == 0:
            temp = 'FizzBuzz'
        print(temp or i)


fizzbuzz(range(1, 101))

"""
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
"""
