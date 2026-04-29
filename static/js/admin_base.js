const toggle = document.getElementById("toggleSidebar");
const sidebar = document.getElementById("sidebar");

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("active");
});

// auto-hide alerts
setTimeout(() => {
    document.querySelectorAll(".alert").forEach(el => el.remove());
}, 3000);