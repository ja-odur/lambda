def left(a):
    def f(b):
        return a
    return f


def right(a):
    def f(b):
        return b
    return f


# context
def add_1(a, b):
    return a + b


def add_2(a):  # Currying
    def f(b):
        return a + b
    return f


def main():
    print(left("5v")("gnd"))
    print(right("5v")("gnd"))
