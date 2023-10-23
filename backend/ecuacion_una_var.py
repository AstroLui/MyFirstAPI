# Archivo contribuido por Annuar :)

import random
from sympy import Symbol
from sympy.solvers import solve

def Termino(x,valor):
    if valor == 1:
        return valor * x
    else:
        return valor

def generarExponenteAleatorio():
    numeros = [1,2,3]
    return random.choice(numeros)

def ecuacionGenerada(t1,t2,t3,ex1,ex2,ex3):
    return f"Ecuacion generada: {t1}**{ex1} + {t2}**{ex2} + {t3}**{ex3} = 0"

def solucionesResultado(t1,t2,t3,ex1,ex2,ex3,x):
    return f"Soluciones: {solve(t1 ** ex1 + t2 ** ex2 + t3 ** ex3,x)}"
