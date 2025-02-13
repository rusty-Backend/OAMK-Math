import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#Palautettavat 6
#Petteri Pätsi

x = sp.symbols('x')

#1.

f = x**2 - 1

#a
f_derivative = sp.diff(f, x)

#b - f

for n in range(-2, 3):
    d_value = f_derivative.subs(x, n)
    print(f"f'({n}) = {d_value}")

#2.

f = 2**x

#a
f_derivative = sp.diff(f, x)

#b - f

for n in range (-2, 3):
    d_value = f_derivative.subs(x, n)
    print(f"f#({n}) = {d_value}")


#3

#a

def f(x):
    return x

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, 2)))

#b

def f(x):
    return x**2

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, 2)))

#c

def f(x):
    return x**3

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, 2)))

#d

def f(x):
    return x**(1/2)

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, 3)))

#4

#a

def f(x):
    return 2**x

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, 2)))

#b

def f(x):
    return 3**2

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, 2)))

#c

def f(x):
    return 0.5**x

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, 2)))


#5

#a

def f(x):
    return sp.sin(x)

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, sp.pi)))

#b

def f(x):
    return sp.cos(x)

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, -(sp.pi)/2, (sp.pi)/2)))

#c

def f(x):
    return sp.sin(x)

x = sp.Symbol("x")
print(sp.integrate(f(x), (x, 0, 2 * sp.pi)))
