import dis


def incr():
    global x
    x += 1


if __name__ == '__main__':
    dis.dis(incr)
