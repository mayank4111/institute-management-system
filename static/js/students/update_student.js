const courseSelect = document.getElementById("courseSelect");
const preview = document.getElementById("coursePreview");
const fee = document.getElementById("courseFee");

courseSelect.addEventListener("change", function () {
    const price = this.options[this.selectedIndex].getAttribute("data-fee");

    if (price) {
        preview.classList.remove("d-none");
        fee.textContent = price;
    } else {
        preview.classList.add("d-none");
    }
});

// photo preview
const photoInput = document.getElementById("photoInput");
const img = document.getElementById("previewImage");

photoInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        img.src = URL.createObjectURL(file);
        img.classList.remove("d-none");
    }
});