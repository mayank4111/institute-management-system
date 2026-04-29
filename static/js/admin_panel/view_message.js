document.addEventListener("DOMContentLoaded", function () {

    const deleteBtn = document.querySelector(".delete-btn");

    if (deleteBtn && !deleteBtn.hasAttribute("disabled")) {
        deleteBtn.addEventListener("click", function (e) {

            const confirmDelete = confirm("This action is irreversible. Do you want to delete this message?");

            if (!confirmDelete) {
                e.preventDefault();
            }

        });
    }

});