const searchInput = document.getElementById("searchInput");
const rows = document.querySelectorAll("#studentTable tbody tr");

function filter() {
    const value = searchInput.value.toLowerCase();

    rows.forEach(row => {
        const name = row.cells[0].innerText.toLowerCase();
        row.style.display = name.includes(value) ? "" : "none";
    });
}

searchInput.addEventListener("input", filter);

document.getElementById("printBtn").onclick = () => window.print();