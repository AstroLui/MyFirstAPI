// JS para Ecuaciones de una sola variable
var global_X = 1
let global_function
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