from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware

from aproximación import *
from integrar import *
from derivar import *

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
    grado = data[0]["grado"]
    derivar(funcion, grado)
    integrar(funcion, grado)
    return data
