const nameInput = document.getElementById("confirmName");
const checkbox = document.getElementById("confirmCheck");
const btn = document.getElementById("deleteBtn");

const studentName = nameInput ? nameInput.getAttribute("data-name") : "";

function validate() {
    const valid = nameInput.value.trim() === studentName && checkbox.checked;
    btn.disabled = !valid;
}

if (nameInput && checkbox) {
    nameInput.addEventListener("input", validate);
    checkbox.addEventListener("change", validate);
}

document.getElementById("deleteForm").addEventListener("submit", function(e) {
    if (btn.disabled) {
        e.preventDefault();
        alert("Complete confirmation first.");
    }
});