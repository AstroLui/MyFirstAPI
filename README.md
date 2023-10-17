# My First API
----
Pasos que se deben de seguir para correr la `Page` de la API
* ### Paso 1:
    Dentro de la carpeta del repositorio abrir la terminal  y crear un entorno virtual. Para mas detalles ir a la pagina [Entorno virtual en python](https://docs.python.org/es/3/tutorial/venv.html)
    ``` 
        python -m venv .venv
    ```

* ###  Paso 2: 
    Inicia el entorno virtual:
    <br>En Windows, ejecuta:
    ```
        .venv\Script\Active.psi
    ```
    En ves de ejecutar lo de antes, hay otra alternativa que es recomendable, es abrir VS Code dentro de la carpeta del repositorio, en la esquina inferior del VS Code les saldra una opcion que dicen `Selecionar Interprete` le dan a esa opcion y les aparecera una ventana de opciones en la parte superior, y seleccionaran la opcion que un lado dice `Recomended`
    <br>En Unix o MacOS, ejecuta:
    ```
        source .venv/bin/active
    ```

* ### Paso 3: 
    Para este paso es valioso que se hallan asegurado que el entorno virtual este activo, para saber si lo esta, deberan abrir una terminal en el VS Code dentro de la carpeta del repositorio, y veran que al principio de la linea de la terminal os aparecera `(.venv)`.
    <br>Una vez que el entorno virtual este activo en la misma terminal instalaran lo siquiente: 
    <br> Primero el `FastAPI`
    ```
        pip install fastapi
    ```
    Luego el `Uvicorn`
    ```
        pip install "uvicorn[standard]"
    ```
    Para una infromacion mas detalla de `FastAPI`, ingresen aqui: [FastAPI](https://fastapi.tiangolo.com/)
* ### Paso 4:
    Despues de haber instalado el `FastAPI` y `Uvicorn` en la terminal colocaran lo siguiente:
    ```
        uvicorn --app-dir backend main:app --reload 
    ```
    y despues abris el `index.html`, eso es todo.

## Instalacion de Requerimientos
Para realizar la instalacion de los requirimientos necesarios colocar en una nueva terminal 
```
    pip install -r requirements.txt
```
Si realizan alguna instalacion nueva para actualizar el archivo requirements.txt colocar 
este comando
```
    pip freeze > requirements.txt
```

## RECORDATORIO:
Abrir el `index.html` con la extension de VS Code `LiveServer` o `LivePreview`


