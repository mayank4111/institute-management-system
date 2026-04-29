// AOS INIT
AOS.init({
    duration: 1000,
    once: true
});

// COUNTER ANIMATION
const counters = document.querySelectorAll(".counter");

const runCounter = (el) => {
    let count = 0;
    const target = +el.dataset.count;

    const update = () => {
        count += target / 50;
        if (count >= target) {
            el.innerText = target;
        } else {
            el.innerText = Math.floor(count);
            requestAnimationFrame(update);
        }
    };

    update();
};

// INTERSECTION OBSERVER
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            counters.forEach(runCounter);
        }
    });
});

const stats = document.querySelector(".stats");
if (stats) observer.observe(stats);