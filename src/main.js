const url = 'http://127.0.0.1:8000'

function useFetch(){
    fetch(url)
    .then(response => response.json())
    .then(data => {
        document.getElementById('Wrapper_Text').innerHTML = data['name']
    })
}

useFetch()