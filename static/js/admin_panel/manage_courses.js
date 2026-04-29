document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");
    const table = document.getElementById("coursesTable");
    const rows = table.getElementsByTagName("tr");

    searchInput.addEventListener("keyup", function () {

        const filter = searchInput.value.toLowerCase();

        for (let i = 1; i < rows.length; i++) {
            const rowText = rows[i].innerText.toLowerCase();
            rows[i].style.display = rowText.includes(filter) ? "" : "none";
        }

    });

});