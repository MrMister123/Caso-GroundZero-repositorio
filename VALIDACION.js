var user=document.getElementById('user');
var password=document.getElementById('password');
var error=document.getElementById('error');

var form=document.getElementById('form');
form.addEventListener('submit', function(evt){
    evt.preventDefault();
    console.log('Enviando formulario...')
    var mensajesError=[];

    if(user.value===null || user.value===''){
        mensajesError.push('Ingresa tu user');
    }

    error.innerHTML = mensajesError.join(', ');
});