document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("deleteForm");

    form.addEventListener("submit", function (e) {
        const confirmDelete = confirm("Are you absolutely sure you want to delete this course?");

        if (!confirmDelete) {
            e.preventDefault();
        }
    });

});