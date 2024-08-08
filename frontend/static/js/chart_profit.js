document.addEventListener('DOMContentLoaded', () => {
    // Получаем JSON данные из элемента script
    const jsonData = document.getElementById('data').textContent;
    const profitData = JSON.parse(jsonData);

    const themeTotals = {};
    profitData.forEach(item => {
        if (themeTotals[item.theme]) {
            themeTotals[item.theme] += item.total;
        } else {
            themeTotals[item.theme] = item.total;
        }
    });

    const themes = Object.keys(themeTotals);
    const totals = Object.values(themeTotals);

    // Создаем график
    const ctx = document.getElementById('profitChart').getContext('2d'); 
    const profitChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: themes,
            datasets: [{
                label: 'Total Profit by Theme',
                data: totals,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    beginAtZero: true
                }
            }
        }
    });
});
