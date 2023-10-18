# Archivo contribuido por Annuar :)

import random
from sympy import Symbol
from sympy.solvers import solve

def generarTerminoAleatorio(x,band):
    valor = random.randint(0,10)
    if band == 0:
        return valor * x
    else:
        return valor

def generarExponenteAleatorio():
    numeros = [1,2,3]
    return random.choice(numeros)

def ecuacionGenerada(t1,t2,t3,ex1,ex2,ex3):
    return f"Ecuacion generada: {t1}**{ex1} + {t2}**{ex2} + {t3}**{ex3} = 0"

def solucionesResultado(t1,t2,t3,ex1,ex2,ex3,x):
    return f"Soluciones: \n{solve(t1 ** ex1 + t2 ** ex2 + t3 ** ex3,x)}"



x = Symbol("x")
var1 = generarTerminoAleatorio(x,random.randint(0,1))
var2 = generarTerminoAleatorio(x,random.randint(0,1))
var3 = generarTerminoAleatorio(x,random.randint(0,1))
exp1 = generarExponenteAleatorio()
exp2 = generarExponenteAleatorio()
exp3 = generarExponenteAleatorio()
ecuacionGenerada(var1,var2,var3,exp1,exp2,exp3)
solucionesResultado(var1,var2,var3,exp1,exp2,exp3,x)