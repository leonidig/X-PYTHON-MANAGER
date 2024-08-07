window.onload = function() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var data = JSON.parse(document.getElementById('data').textContent);
    var labels = data.map(function(item) { return item.date; });
    var totals = data.map(function(item) { return item.total; });
    
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Total',
                data: totals,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
};
