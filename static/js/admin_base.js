// admin_base.js

document.addEventListener("DOMContentLoaded", function () {
    console.log("Admin Base Loaded");

    // Auto-hide alerts
    setTimeout(() => {
        let alerts = document.querySelectorAll(".alert");
        alerts.forEach(alert => {
            alert.style.transition = "opacity 0.5s";
            alert.style.opacity = "0";
            setTimeout(() => alert.remove(), 500);
        });
    }, 3000);
});