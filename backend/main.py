from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins=[
    "http://localhost:3000",
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3000/src/pages/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/apro-fun")
async def Prueba():
    x=[1, 2, 3, 4]
    return {
        "Problema": {
            "Enunciado": x
        }
    }