document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("addCourseForm");

    form.addEventListener("submit", function (e) {
        const fee = document.querySelector("input[name='fee']").value;

        if (fee <= 0) {
            alert("Fee must be greater than 0");
            e.preventDefault();
        }
    });

});