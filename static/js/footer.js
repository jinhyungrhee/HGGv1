window.addEventListener("load", loadEventHandler);
function loadEventHandler() {
    var footer = document.querySelector("footer");
    var rect = footer.getBoundingClientRect();
    var height = document.documentElement.scrollHeight - rect.bottom;
    if (rect.bottom < document.documentElement.scrollHeight - 10) {
        footer.style.position = "relative";
        footer.style.bottom = `-${height}px`;
    }
}
