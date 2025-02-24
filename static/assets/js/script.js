function docLoaded(){
    userFormsBtn = document.getElementById("login-signup-link");

    try {
        userFormsBtn.addEventListener("click", e => {
            document.getElementById("login-form-container").classList.toggle("hidden");
        });
    }
    catch {} // when user is logged in "userFormsBtn" isn't in the document,
             // this prevents error from stopping the script

    document.getElementById("popup-close-button").addEventListener("click", e =>{
        document.getElementById("popup-message").classList.toggle("hidden");
    })
}

document.onload = docLoaded();