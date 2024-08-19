def TRUE(x):
    return lambda y: x


def FALSE(x):
    return lambda y: y


def NOT(x):
    return x(FALSE)(TRUE)


assert NOT(TRUE) is FALSE
assert NOT(FALSE) is TRUE


def AND(x):
    return lambda y: x(y)(x)


assert AND(TRUE)(TRUE) is TRUE
assert AND(TRUE)(FALSE) is FALSE
assert AND(FALSE)(TRUE) is FALSE
assert AND(FALSE)(FALSE) is FALSE


def OR(x):
    return lambda y: x(x)(y)


assert OR(TRUE)(TRUE) is TRUE
assert OR(TRUE)(FALSE) is TRUE
assert OR(FALSE)(TRUE) is TRUE
assert OR(FALSE)(FALSE) is FALSE
