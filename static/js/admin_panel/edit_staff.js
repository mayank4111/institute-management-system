document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("editStaffForm");
    const photoInput = document.getElementById("photoInput");
    const preview = document.getElementById("newPhotoPreview");
    const experienceInput = document.getElementById("experienceInput");

    const initialData = new FormData(form);

    // Image preview + validation
    photoInput.addEventListener("change", function () {
        const file = this.files[0];

        if (file) {
            if (file.size > 2 * 1024 * 1024) {
                alert("Image must be less than 2MB");
                this.value = "";
                return;
            }

            preview.src = URL.createObjectURL(file);
            preview.classList.remove("d-none");
        }
    });

    // Form validation
    form.addEventListener("submit", function (e) {

        const experience = parseInt(experienceInput.value);

        if (experience < 0) {
            alert("Experience cannot be negative");
            e.preventDefault();
            return;
        }

        // Detect no changes
        const currentData = new FormData(form);
        let changed = false;

        for (let [key, value] of currentData.entries()) {
            if (value !== initialData.get(key)) {
                changed = true;
                break;
            }
        }

        if (!changed) {
            alert("No changes detected");
            e.preventDefault();
        }

    });

});