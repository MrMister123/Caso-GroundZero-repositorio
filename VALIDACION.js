/*var user=document.getElementById('user');
var correo=document.getElementById('correo');
var password=document.getElementById('password');
error.style.color='red';

var form=document.getElementById('formulario');
form.addEventListener('submit', function(evt){
    evt.preventDefault();
    console.log('Enviando formulario...')
    var mensajesError=[];

    if(user.value===null || user.value===''){
        mensajesError.push('Ingresa tu nombre de usuario');
    }else{
        if(user.value.length<3 || user.value.length>20){
            mensajesError.push('El largo de tu nombre de usuario debe estar entre 3 y 20 caracteres');
        }
    }

    if(correo.value===null || correo.value===''){
        mensajesError.push('Ingresa tu correo electronico')
    }

    if(password.value===null || password.value===''){
            mensajesError.push('Ingresa tu contraseña');
    }

   
    error.innerHTML = mensajesError.join(', ');
});*/

const user = document.getElementById('user')
const correo = document.getElementById('correo')
const pass = document.getElementById('password')
const form = document.getElementById('formulario')
const parrafo = document.getElementById('error')
form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    parrafo.innerHTML = ""
    if(user.value.length < 6){
        warnings += `El nombre no es valido <br>` 
        entrar = true
    }
    if(!regexEmail.test(correo.value)){
        warnings += `El correo no es valido <br>` 
        entrar = true
    }
    if (pass.value.length < 8){
        warnings += `La contraseña no es valido <br>` 
        entrar = true
    }

    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = `form validado`
    }
});