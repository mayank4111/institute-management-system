document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("staffForm");

    form.addEventListener("submit", function (e) {

        const experience = document.querySelector("input[name='experience']").value;

        if (experience < 0) {
            alert("Experience cannot be negative");
            e.preventDefault();
        }

    });

});