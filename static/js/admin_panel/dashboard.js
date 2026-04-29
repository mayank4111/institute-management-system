document.addEventListener("DOMContentLoaded", function () {

    // Pie Chart
    new Chart(document.getElementById('enrollmentChart'), {
        type: 'pie',
        data: {
            labels: enrollmentData.labels,
            datasets: [{
                data: enrollmentData.data,
                backgroundColor: ['#667eea', '#764ba2', '#f093fb', '#f5576c']
            }]
        }
    });

    // Line Chart
    new Chart(document.getElementById('admissionChart'), {
        type: 'line',
        data: {
            labels: ['Jan','Feb','Mar','Apr','May','Jun'],
            datasets: [{
                label: 'Admissions',
                data: monthlyData,
                borderColor: '#667eea',
                fill: true
            }]
        }
    });

});