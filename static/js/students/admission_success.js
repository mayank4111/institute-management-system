// small animation polish
document.querySelectorAll(".glass-inner").forEach((el, i) => {
    setTimeout(() => {
        el.style.opacity = 1;
        el.style.transform = "translateY(0)";
    }, i * 100);
});