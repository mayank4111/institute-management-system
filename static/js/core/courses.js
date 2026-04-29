AOS.init({ duration: 1000 });

const searchInput = document.getElementById('searchCourse');
const categoryFilter = document.getElementById('categoryFilter');
const sortBy = document.getElementById('sortBy');
const courseGrid = document.getElementById('courseGrid');

let courses = Array.from(document.querySelectorAll('.course-item'));

function filterCourses() {
    const searchTerm = searchInput.value.toLowerCase();
    const category = categoryFilter.value;

    let filtered = courses.filter(c => {
        return (
            c.dataset.name.includes(searchTerm) &&
            (category === 'all' || c.dataset.category === category)
        );
    });

    if (sortBy.value === 'fee_low') {
        filtered.sort((a, b) => a.dataset.fee - b.dataset.fee);
    } else if (sortBy.value === 'fee_high') {
        filtered.sort((a, b) => b.dataset.fee - a.dataset.fee);
    }

    courseGrid.innerHTML = "";
    filtered.forEach(c => courseGrid.appendChild(c));
}

searchInput.addEventListener("input", filterCourses);
categoryFilter.addEventListener("change", filterCourses);
sortBy.addEventListener("change", filterCourses);