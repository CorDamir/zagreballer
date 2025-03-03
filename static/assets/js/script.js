function closePopup(){ this.classList.toggle("hidden"); }

function toggleMenu(){
    MENU.classList.toggle("open");
    this.classList.toggle("reverse-toggler");
}

function displayConfirmationModal(){
    MODAL.classList.toggle("hidden");
    link = this.getAttribute("data-action");
    console.log(link);
}

function docLoaded(){
    document.getElementById("popup-message").addEventListener("click", closePopup);
    document.getElementById("menu-toggler").addEventListener("click", toggleMenu);

    YES.addEventListener("click", () => {
        if (link) window.location.href = link;
        else postForm = document.getElementsByTagName("form")[0].submit();
       });

    NO.addEventListener("click", () => {
        MODAL.classList.toggle("hidden");
    });
    
    for (let el of document.getElementsByClassName("modal-activator")){
        el.addEventListener("click", displayConfirmationModal);
    }
}

const MENU = document.getElementById("menu-options");
const YES = document.getElementById("yes");
const NO = document.getElementById("no");
const MODAL = document.getElementById("modal-container");
let link = "";
let postForm = null;

document.onload = docLoaded();