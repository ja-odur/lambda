ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))


def incr(x):
    return x + 1  # Illegal in rule. Only for demo purposes


print(incr(0))  # outputs 1
print(incr(incr(0)))  # outputs 2
print(incr(incr(incr(0))))  # outputs 3

print(THREE(incr)(0))  # outputs 3 too!!


def p(t):
    return t[0]+1, t[0]


print(p((0, 0)))  # outputs (1, 0)
print(p(p(p((0, 0)))))  # outputs (3, 2)
print(THREE(p)((0, 0)))  # outputs (3, 2) too!!

a = FOUR(THREE)  # 3 ** 4

print(a(incr)(0))  # outputs 81

# How do you represent zero?
ZERO = lambda f: lambda x: x  # No function call of f. Equivalent of FALSE.

# How do go beyond four?
# Challenge: Implement successor
# SUCC(TWO) ---> THREE
SUCC = lambda n: (lambda f: lambda x: f(n(f)(x)))

FIVE = SUCC(FOUR)

print(FIVE(incr)(0))  # outputs 5


def PRINT_NUMBER(num):
    print(num(incr)(0))
