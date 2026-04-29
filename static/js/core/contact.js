AOS.init({
    duration: 1000,
    once: true
});

// FORM VALIDATION
document.getElementById("contactForm").addEventListener("submit", function(e) {
    const fields = this.querySelectorAll("input[required], textarea[required]");
    let valid = true;

    fields.forEach(f => {
        if (!f.value.trim()) valid = false;
    });

    if (!valid) {
        e.preventDefault();
        alert("Please fill all required fields");
    }
});