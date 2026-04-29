document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("loginForm");

    form.addEventListener("submit", function () {

        const button = document.querySelector(".btn-login");
        button.innerHTML = "Logging in...";
        button.disabled = true;

    });

});
