const loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", (e) => {
    e.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Obtiene los valores del usuario y contraseña
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Aquí puedes implementar la lógica para autenticar al usuario
    // Por ejemplo, puedes enviar los datos a un servidor mediante una solicitud fetch() o axios.

    // Por ahora, solo mostraremos los valores en la consola como ejemplo
    console.log("Usuario: ", username);
    console.log("Contraseña: ", password);
});
