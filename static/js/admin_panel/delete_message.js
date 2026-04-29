document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("deleteMessageForm");

    form.addEventListener("submit", function (e) {

        const confirmDelete = confirm("This action is irreversible. Continue?");

        if (!confirmDelete) {
            e.preventDefault();
        }

    });

});