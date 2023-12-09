function togglePassword() {
    var senhaInput = document.getElementById("senhaInput");
    var tipoAtual = senhaInput.type;

    // Alterna entre "password" e "text"
    senhaInput.type = tipoAtual === "password" ? "text" : "password";
}