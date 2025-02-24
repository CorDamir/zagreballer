function docLoaded(){
    document.getElementById("login-signup-link").addEventListener("click", e => {
        document.getElementById("login-form-container").classList.toggle("hidden");
    });

    document.getElementById("popup-close-button").addEventListener("click", e =>{
        document.getElementById("popup-message").classList.toggle("hidden");
    })
}

document.onload = docLoaded();