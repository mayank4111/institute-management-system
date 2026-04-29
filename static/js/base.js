// AOS
AOS.init({
    duration: 1000
});

// Navbar scroll effect
window.addEventListener("scroll", () => {
    const nav = document.querySelector(".custom-navbar");
    if (window.scrollY > 50) {
        nav.style.background = "#000";
    } else {
        nav.style.background = "rgba(0,0,0,0.6)";
    }
});

// auto hide alerts
setTimeout(() => {
    document.querySelectorAll(".alert").forEach(el => el.remove());
}, 3000);