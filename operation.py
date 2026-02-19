import math


# Basic operations
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Power operations
def square(x):
    return x * x


def cube(x):
    return x * x * x


def power(x, y):
    return math.pow(x, y)


# Roots
def square_root(x):
    if x < 0:
        raise ValueError("Square root of negative number is not allowed")
    return math.sqrt(x)


def cube_root(x):
    return x ** (1/3)


# Trigonometric
def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


# Inverse trigonometric
def asin(x):
    return math.degrees(math.asin(x))


def acos(x):
    return math.degrees(math.acos(x))


def atan(x):
    return math.degrees(math.atan(x))


# Logarithmic
def log10(x):
    if x <= 0:
        raise ValueError("Log input must be greater than 0")
    return math.log10(x)


def ln(x):
    if x <= 0:
        raise ValueError("Log input must be greater than 0")
    return math.log(x)


def antilog(x):
    return math.pow(10, x)
