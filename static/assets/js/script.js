function closePopup(){ this.classList.toggle("hidden"); }
function toggleMenu(e){ if (e.target == this) this.classList.toggle("open") }

function displayConfirmationModal(){
    MODAL.classList.toggle("hidden");
    link = this.getAttribute("data-action");
}

function docLoaded(){
    document.getElementById("popup-message").addEventListener("click", closePopup);
    document.getElementById("menu-options").addEventListener("click", toggleMenu);

    YES.addEventListener("click", () => {
        postForm = document.getElementsByTagName("form")[0];
        if (postForm) postForm.submit();
        else window.location.href = link;
    })

    NO.addEventListener("click", () => {
        MODAL.classList.toggle("hidden");
    })
    
    for (el of document.getElementsByClassName("modal-activator")) 
        el.addEventListener("click", displayConfirmationModal);
}

const YES = document.getElementById("yes");
const NO = document.getElementById("no");
const MODAL = document.getElementById("modal-container");
let link = "";
document.onload = docLoaded();