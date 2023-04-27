const form = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const validator = /^[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{1,5}/

const validarForm = (e) => {
    switch (e.target.name){
        case "correo":
            if(validator.test(e.target.value)){
                document.getElementById('prueba').classList.add('icon-correct');
            }else if(e.target.value == ""){
                document.getElementById('lblcorreo').classList.remove('txt_field-up');
            } 
            else{
                document.getElementById('lblcorreo').classList.add('txt_field-up');
            }
        break;
    };
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarForm);
    input.addEventListener('blur', validarForm);
});

form.addEventListener('submit', (e) =>{
    e.preventDefault();
});