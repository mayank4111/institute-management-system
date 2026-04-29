document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("editCourseForm");
    const feeInput = document.getElementById("feeInput");
    const imageInput = document.getElementById("imageInput");
    const pdfInput = document.getElementById("pdfInput");
    const preview = document.getElementById("newImagePreview");
    const submitBtn = document.getElementById("submitBtn");

    const initialData = new FormData(form);

    // Image preview
    imageInput.addEventListener("change", function () {
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

    // PDF validation
    pdfInput.addEventListener("change", function () {
        const file = this.files[0];

        if (file) {
            if (file.type !== "application/pdf") {
                alert("Only PDF allowed");
                this.value = "";
                return;
            }

            if (file.size > 5 * 1024 * 1024) {
                alert("PDF must be less than 5MB");
                this.value = "";
            }
        }
    });

    // Form validation
    form.addEventListener("submit", function (e) {

        const fee = parseFloat(feeInput.value);

        if (fee < 0) {
            alert("Fee cannot be negative");
            e.preventDefault();
        }

        // Check if no changes made
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