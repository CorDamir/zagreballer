function docLoaded(){
    document.getElementById("login-signup-link").addEventListener("click", e => {
        document.getElementById("login-form-container").classList.toggle("hidden");
    });
}

document.onload = docLoaded();