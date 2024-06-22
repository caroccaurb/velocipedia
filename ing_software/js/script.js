function validarFormulario() {
    let nombre = document.getElementById("regNombre").value;
    let usuario = document.getElementById("regUsuario").value;
    let apellido = document.getElementById("regApellido").value;
    let email = document.getElementById("regEmail").value;
    let telefono = document.getElementById("regTelefono").value;
    let passwd = document.getElementById("passwd").value;
    let passwd2 = document.getElementById("passwd2").value;


    if(nombre === "") {
        document.getElementById("msgNombre").innerText = "Ingrese un nombre valido";
    } else {
        document.getElementById("msgNombre").innerText = "";
    }
    if(usuario === "") {
        document.getElementById("msgUsuario").innerText = "Ingrese un Usuario valido";
    } else {
        document.getElementById("msgUsuario").innerText = "";
    }

    if(apellido === "") {
        document.getElementById("msgApellido").innerText = "Ingrese un apellido valido";
    } else {
        document.getElementById("msgApellido").innerText = "";
    }

    if (email ==="" ) {
        document.getElementById("msgEmail").innerText = "Ingrese un email valido";
    } else {
        document.getElementById("msgEmail").innerText = "";
    }

    if (telefono ==="" ) {
        document.getElementById("msgTel").innerText = "Ingrese un telefono valido";
    } else {
        document.getElementById("msgTel").innerText = "";
    }

    if (passwd ==="" ) {
        document.getElementById("msgpass1").innerText = "Por favor ingrese una contraseña";
    } else {
        document.getElementById("msgpass1").innerText = "";
    }

    if (passwd2 === ""){
        document.getElementById("msgpass2").innerText = "Por favor confirme la contraseña";
      
    }
    if(passwd2 !== passwd){
        document.getElementById("msgpass2").innerText = "Las contraseñas deben ser iguales";
    } else{
        document.getElementById("msgpass2").innerText = "";
    }

    if (nombre === "" || apellido === "" || usuario === "" || email === "" || telefono === "" || passwd === "" || passwd2 === "") {
        btnsubmit.disabled = true; // Deshabilitar el botón de envío
    } else {
        btnsubmit.disabled = false; // Habilitar el botón de envío
    }
}