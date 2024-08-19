from .O3_numbers import THREE, FOUR, SUCC, PRINT_NUMBER


ADD = lambda x: lambda y: y(SUCC)(x)

PRINT_NUMBER(ADD(FOUR)(THREE))  # outputs 7

MUL = lambda x: lambda y: lambda f: y(x(f))

PRINT_NUMBER(MUL(FOUR)(THREE))  # outputs 12
