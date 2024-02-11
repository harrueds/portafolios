// hola-mundo.js
document.addEventListener('DOMContentLoaded', function () {
    // El código dentro de esta función se ejecutará cuando la página haya cargado completamente

    // Muestra "Hola, mundo!" en la consola del navegador
    console.log("Hola mundo");

    // Muestra "Hola, mundo!" en un cuadro de alerta
    alert("Hola Mundo");

    // Muestra "Hola, mundo!" en el cuerpo de la página
    var mensaje = document.createElement('p');
    mensaje.textContent = "Hola, mundo!";
    document.body.appendChild(mensaje);
});
