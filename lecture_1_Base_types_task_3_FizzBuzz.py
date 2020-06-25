def fizzbuzz(*args):
    """
    Instead of numbers that are multiples of three, the program should
    output the word Fizz, and instead of numbers divisible by five,
    the word Buzz. If the number is a multiple of 3 and 5, then the
    program should output the word FizzBuzz.
    :param args: Numbers range
    :return: Print result
    """
    result = []
    for i in args:
        if not isinstance(i, int):
            raise ValueError("Value Error")
        temp = ''
        if i % 3 == 0:
            temp = 'Fizz'
        if i % 5 == 0:
            temp = 'Buzz'
        if i % 15 == 0:
            temp = 'FizzBuzz'
        result.append(temp or i)
    return result
