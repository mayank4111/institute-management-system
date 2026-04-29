let step = 1;
const totalSteps = 4;

function showStep(n) {
    document.querySelectorAll(".form-step").forEach((el, i) => {
        el.classList.toggle("active", i === n - 1);
    });

    document.querySelectorAll(".step").forEach((el, i) => {
        el.classList.toggle("active", i === n - 1);
    });

    document.getElementById("prevBtn").style.display = n === 1 ? "none" : "inline-block";

    if (n === totalSteps) {
        document.getElementById("nextBtn").classList.add("d-none");
        document.getElementById("submitBtn").classList.remove("d-none");
        updatePreview();
    } else {
        document.getElementById("nextBtn").classList.remove("d-none");
        document.getElementById("submitBtn").classList.add("d-none");
    }
}

document.getElementById("nextBtn").onclick = () => {
    if (step < totalSteps) showStep(++step);
};

document.getElementById("prevBtn").onclick = () => {
    if (step > 1) showStep(--step);
};

function updatePreview() {
    const name = document.querySelector('[name="name"]').value;
    const email = document.querySelector('[name="email"]').value;

    document.getElementById("previewContent").innerHTML =
        `<p><strong>Name:</strong> ${name}</p>
         <p><strong>Email:</strong> ${email}</p>`;
}

showStep(step);