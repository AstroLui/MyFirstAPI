// JS para Aproximacion de funciones
var global_XY = 2
function __A_Plus(){
    const old_X = document.getElementById('X').innerHTML
    const old_Y = document.getElementById('Y').innerHTML
    document.getElementById('X').innerHTML = `
    ${old_X}
    <div id="inputs">
        <input type="number" placeholder="1"/>
    </div>
    `
    document.getElementById('Y').innerHTML = `
    ${old_Y}
    <div id="inputs">
        <input type="number" placeholder="1"/>
    </div>
    `
}
function A_Add_Plus(){
    if(global_XY < 4){
        global_XY = global_XY + 1
        __A_Plus()
    }
}
function __A_Minus(){
    const A_Minus_X = document.getElementById('X').querySelectorAll('#inputs') 
    const A_Minus_Y = document.getElementById('Y').querySelectorAll('#inputs')
    document.getElementById('X').removeChild(A_Minus_X[A_Minus_X.length-1])
    document.getElementById('Y').removeChild(A_Minus_Y[A_Minus_Y.length-1])
}
function A_Delete_Minus(){
    if(global_XY > 2){
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
