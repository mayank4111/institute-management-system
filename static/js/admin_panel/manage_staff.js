document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");
    const table = document.getElementById("staffTable");
    const rows = table.getElementsByTagName("tr");

    // Search
    searchInput.addEventListener("keyup", function () {
        const filter = searchInput.value.toLowerCase();

        for (let i = 1; i < rows.length; i++) {
            const text = rows[i].innerText.toLowerCase();
            rows[i].style.display = text.includes(filter) ? "" : "none";
        }
    });

    // Delete confirmation
    document.querySelectorAll(".delete-btn").forEach(btn => {
        btn.addEventListener("click", function (e) {
            if (!confirm("Are you sure you want to delete this staff member?")) {
                e.preventDefault();
            }
        });
    });

});