// JS para Aproximacion de funciones
var global_XY = 5
function __Post(global_Array_X, global_Array_Y){
    document.querySelectorAll('#inputs-X').forEach(input =>{
        if(input.querySelector('input').value == ''){
            global_Array_X.push(parseInt(input.querySelector('input').placeholder))
        }else{
            global_Array_X.push(parseInt(input.querySelector('input').value))
        }
    })
    document.querySelectorAll('#inputs-Y').forEach(input =>{
        if(input.querySelector('input').value == ''){
            global_Array_Y.push(parseInt(input.querySelector('input').placeholder))
        }else{
            global_Array_Y.push(parseInt(input.querySelector('input').value))
        }
    })

}
async function A_PostFetch(){
    const global_Array_X = []
    const global_Array_Y = []
    const opcion= document.getElementById('Title-Select').innerText;
    __Post(global_Array_X, global_Array_Y)
    const JSON_Request = [
        {
            "X": global_Array_X,
            "Y": global_Array_Y,
            "opcion": opcion
        }
    ];
    let response = await fetch('http://127.0.0.1:8000/solucion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
        body: JSON.stringify(JSON_Request)
    });
    let resutl = await response.json()
}
function __A_Plus(){
    const old_X = document.getElementById('X').innerHTML
    const old_Y = document.getElementById('Y').innerHTML
    document.getElementById('X').innerHTML = `
    ${old_X}
    <div id="inputs-X">
        <input type="number" placeholder="1"/>
    </div>
    `
    document.getElementById('Y').innerHTML = `
    ${old_Y}
    <div id="inputs-Y">
        <input type="number" placeholder="1"/>
    </div>
    `
}
function A_Add_Plus(){
    if(global_XY < 8){
        global_XY = global_XY + 1
        __A_Plus()
    }
}
function __A_Minus(){
    const A_Minus_X = document.getElementById('X').querySelectorAll('#inputs-X') 
    const A_Minus_Y = document.getElementById('Y').querySelectorAll('#inputs-Y')
    document.getElementById('X').removeChild(A_Minus_X[A_Minus_X.length-1])
    document.getElementById('Y').removeChild(A_Minus_Y[A_Minus_Y.length-1])
}
function A_Delete_Minus(){
    if(global_XY > 5){
        __A_Minus()
        global_XY = global_XY - 1
    }
}
function Pass(){
    const old = document.getElementById('Title-Select').innerHTML
    const _new = document.getElementById('Nav-Select-P').innerHTML
    document.getElementById('Title-Select').innerHTML = _new
    document.getElementById('Nav-Select-P').innerHTML = old
    Nav_Active()
}
function Nav_Active(){
    const inputs = document.getElementById('Nav-Select-Op').querySelectorAll('div')
    inputs.forEach(input =>{
        if(input.classList.contains('Nav-Active')){
            input.classList.remove('Nav-Active')
            document.getElementById('Nav-Select').style.height = '4vh'
        }else{
            input.classList.add('Nav-Active')
            document.getElementById('Nav-Select').style.height = '85px'
            
        }

    })
}
// JS para Ecuaciones de una sola variable
var global_X = 1
function __Plus(sup){
    const old = document.getElementById('infuncion').innerHTML
    document.getElementById('infuncion').innerHTML = `
    <div id="frag"><input id="coeficiente" class="coeficiente" type="number" max="100" placeholder="1"/><span id="variable">X <sup>${sup}</sup> + </span></div>
    ${old}`
}
function Add_Plus(){
    if(global_X <=4){
        global_X = global_X + 1
        __Plus(global_X)
    }
}

function __Minus(){
    const __Minus = document.getElementById('infuncion').querySelectorAll("#frag")
    document.getElementById('infuncion').removeChild(__Minus[0])

}
function Delete_Minus(){
    if(global_X != 1){
        __Minus()
        global_X = global_X - 1
    }
}
function __Calcular(){

}
function Calcular(){
    document.getElementById('B-Calcular').style.backgroundColor= 'gray'
    setTimeout(()=>{document.getElementById('B-Calcular').style.backgroundColor= 'white'}, 200)
}
// JS para Diferencion e integracion numerica
var I_global_X = 1
function __I_Post(Array){
    const inputs = document.querySelector('#InFuncion').querySelectorAll('div')
    var x = 0
    inputs.forEach(input => {
        if(input.querySelector('input').value == ''){
            Array.push(`x**${inputs.length-x}`)
            x = x + 1
        }else{
            Array.push(`${input.querySelector('input').value}x**${inputs.length-x}`)
            x = x + 1
        }
    })
}
async function I_PostFetch(){
    const Array = []
    __I_Post(Array)
    const JSON_Request = [{
        "funcion" : parseInt(Array.join('+')),
        "grado" : Array.length,
    }];
    const response = await fetch('http://127.0.0.1:8000/solucionIntegral', {
        method: 'POST',
        headers:{'Content-type': 'application/json;charset=utf-8'},
        body: JSON.stringify(JSON_Request)
    })
    const result = await response.json()
    console.log(result)
}
function __I_Plus(sup){
    const old = document.getElementById('InFuncion').innerHTML
    document.getElementById('InFuncion').innerHTML = `
    <div id="frag"><input id="coeficiente" class="coeficiente" type="number" max="100" placeholder="1"/><span id="variable_Integral">X <sup>${sup}</sup> + </span></div>
    ${old}`
}
function I_Add_Plus(){
    if(I_global_X < 4){
       I_global_X = I_global_X + 1
        __I_Plus(I_global_X)
    }
}
function __I_Minus(){
    const __Minus = document.getElementById('InFuncion').querySelectorAll("#frag")
    document.getElementById('InFuncion').removeChild(__Minus[0])
}
function I_Delete_Minus(){
    if(I_global_X != 1){
        __I_Minus()
        I_global_X = I_global_X - 1
    }
}

// JS para Ecuaciones Diferenciales
