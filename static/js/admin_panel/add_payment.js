document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("paymentForm");
    const amountInput = document.querySelector("input[name='amount']");

    form.addEventListener("submit", function (e) {

        const maxAmount = parseFloat(amountInput.max);
        const enteredAmount = parseFloat(amountInput.value);

        if (enteredAmount > maxAmount) {
            alert("Amount cannot exceed remaining fee!");
            e.preventDefault();
        }

        if (enteredAmount <= 0) {
            alert("Amount must be greater than 0");
            e.preventDefault();
        }

    });

});