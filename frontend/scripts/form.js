$(document).ready(function () {
    const open = document.querySelector("[data-open-modal]");
    const close = document.querySelector("[data-close-modal]");
    const modal = document.querySelector("[data-modal]");
    open.addEventListener("click", () => {
        modal.showModal()
    });
    close.addEventListener("click", () =>{
        modal.close()
    });
});