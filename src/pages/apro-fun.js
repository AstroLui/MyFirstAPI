function Apro_Fun(){
    const url = "http://127.0.0.1:8000/apro-fun"
    fetch(url)
    .then(response => response.json())
    .then(data => {
        document.getElementById('Ejercicio').innerHTML = `Resolver de manera genial este array ${data["Problema"]["Enunciado"]}`
    })
}
Apro_Fun()