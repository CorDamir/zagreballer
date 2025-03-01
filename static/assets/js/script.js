function closePopup(){ this.classList.toggle("hidden"); }
function toggleMenu(e){ if (e.target == this) this.classList.toggle("open") }

function docLoaded(){
    document.getElementById("popup-message").addEventListener("click", closePopup);
    document.getElementById("menu-options").addEventListener("click", toggleMenu);
}

document.onload = docLoaded();