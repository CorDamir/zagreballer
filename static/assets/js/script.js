function closePopup(){ this.classList.toggle("hidden"); }

function toggleMenu(){
    MENU.classList.toggle("open");
    this.classList.toggle("reverse-toggler");
}

function displayConfirmationModal(){
    postForm = document.getElementsByTagName("form")[0];
    link = this.getAttribute("data-action");

    if (link) MODAL.classList.toggle("hidden");
    else if (postForm) {
        if (postForm.checkValidity()) MODAL.classList.toggle("hidden");
        else postForm.reportValidity();
        }
}

function docLoaded(){
    MENU = document.getElementById("menu-options");
    YES = document.getElementById("yes");
    NO = document.getElementById("no");
    MODAL = document.getElementById("modal-container");
    link = "";
    postForm = null;

    document.getElementById("popup-message").addEventListener("click", closePopup);
    document.getElementById("menu-toggler").addEventListener("click", toggleMenu);

    YES.addEventListener("click", () => {
        if (link) window.location.href = link;
        else postForm.submit();
       });

    NO.addEventListener("click", () => {
        MODAL.classList.toggle("hidden");
    });
    
    for (let el of document.getElementsByClassName("modal-activator")){
        el.addEventListener("click", displayConfirmationModal);
    }
}

let MENU, YES, NO, MODAL, link, postForm;
document.addEventListener("DOMContentLoaded", docLoaded);