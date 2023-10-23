# My First API
----
Pasos que se deben de seguir para correr la `Page` de la API
* ### Paso 1:
    Dentro de la carpeta del repositorio abrir la terminal y crear un entorno virtual. Para más detalles ir a la página [Entorno virtual en python](https://docs.python.org/es/3/tutorial/venv.html)
    ``` 
        python -m venv .venv
    ```

* ###  Paso 2: 
    Inicia el entorno virtual:
    <br>En Windows, ejecuta:
    ```
        .venv\Script\Active.psi
    ```
    En vez de ejecutar el paso anterior, hay otra opción que es recomendable, esta es abrir VS Code dentro de la carpeta del repositorio, en la esquina inferior del VS Code les saldra una opción que dicen `Selecionar Interprete` le dan a esa opción y les aparecerá una ventana de opciones en la parte superior, y seleccionarán la opción que un lado dice `Recomended`
    <br>En Unix o MacOS, ejecuta:
    ```
        source .venv/bin/active
    ```

* ### Paso 3: 
    Para este paso es valioso que se hayan asegurado que el entorno virtual este activo, para saber si lo está, deberán abrir una terminal en el VS Code dentro de la carpeta del repositorio, y verán que al principio de la línea de la terminal os aparecera `(.venv)`.
    <br>Una vez que el entorno virtual esté activo en la misma terminal instalarán lo siquiente: 
    <br> Primero el `FastAPI`
    ```
        pip install fastapi
    ```
    Luego el `Uvicorn`
    ```
        pip install "uvicorn[standard]"
    ```
    Para una infromación más detallada de `FastAPI`, ingresen aquí: [FastAPI](https://fastapi.tiangolo.com/)
* ### Paso 4:
    Después de haber instalado el `FastAPI` y `Uvicorn` en la terminal colocarán lo siguiente:
    ```
        uvicorn --app-dir backend main:app --reload 
    ```
    y después abris el `index.html`, eso es todo.

## Instalación de Requerimientos
Para realizar la instalación de los requirimientos necesarios colocar en una nueva terminal 
```
    pip install -r requirements.txt
```
Si realizan alguna instalación nueva para actualizar el archivo requirements.txt colocar 
este comando
```
    pip freeze > requirements.txt
```

## RECORDATORIO:
Abrir el `index.html` con la extension de VS Code `LiveServer` o `LivePreview`


