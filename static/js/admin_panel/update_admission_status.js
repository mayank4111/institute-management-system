document.addEventListener("DOMContentLoaded", function () {

    const statusSelect = document.getElementById("statusSelect");
    const warningBox = document.getElementById("warningBox");
    const form = document.getElementById("statusForm");

    // Dynamic warnings
    statusSelect.addEventListener("change", function () {

        const value = this.value;

        if (value === "cancelled") {
            warningBox.classList.remove("d-none");
        } else {
            warningBox.classList.add("d-none");
        }

    });

    // Confirm on dangerous action
    form.addEventListener("submit", function (e) {

        if (statusSelect.value === "cancelled") {
            const confirmDelete = confirm("Are you sure? This will cancel the admission permanently.");

            if (!confirmDelete) {
                e.preventDefault();
            }
        }

    });

});