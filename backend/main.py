from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware

from aproximación import *
from integrar import *
from derivar import *
from edo import calcEDO
from ecuacion_una_var import *

app = FastAPI()
origins=[
    "http://localhost:3000",
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3000/src/pages/apro-fun.html"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/solucion")
async def A_Post(request: Request):
    data = await request.json()
    Array_X = data[0]["X"]
    Array_Y = data[0]["Y"]
    opcion = data[0]["opcion"]
    if opcion == "Recta": 
        recta(np.array(Array_X), np.array(Array_Y))
    else:
        parabola(np.array(Array_X),np.array(Array_Y))
    return 

@app.post("/solucionIntegral")
async def I_Post(request: Request): 
    data = await request.json()
    funcion = data[0]["funcion"]
    integral(funcion)
    derivar(funcion)
    return data

@app.post("/solucionEuacionI")
async def Ei_Post(request: Request): 
    data = await request.json()
    X = data[0]["funcion-X"]
    Y = data[0]["funcion-Y"]
    X_ini = data[0]["X-inicial"]
    Y_ini = data[0]["Y-inicial"]
    N = data[0]["N"]
    H = data[0]["H"]
    Var_X = X[0]
    Coe_X = X[1]
    Var_Y = Y[0]
    Coe_Y = Y[1]
    calcEDO(X_ini, Y_ini, H, N, Var_X, Coe_X, Var_Y, Coe_Y)
    return data

@app.post("/solucionEcuacionV")
async def V_Post(request: Request):
    data = await request.json()
    coef = data[0]["coeficientes"]
    exp = data[0]["exponente"]
    x = Symbol("x")
    ecuacion = ecuacionGenerada(Termino(x, coef[0]),Termino(x, coef[1]),Termino(x, coef[2]),exp[0],exp[1],exp[2])
    solucion = solucionesResultado(Termino(x, coef[0]),Termino(x, coef[1]),Termino(x, coef[2]),exp[0],exp[1],exp[2],x)
    return {
        "ecuacion" : ecuacion,
        "solucion" : solucion
    }
    