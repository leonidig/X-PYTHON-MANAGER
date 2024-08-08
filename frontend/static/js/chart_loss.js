document.addEventListener('DOMContentLoaded', () => {
    // Получаем JSON данные из элемента script
    const jsonData = document.getElementById('data').textContent;
    const lossData = JSON.parse(jsonData);

    // Группируем данные по теме и суммируем общие суммы
    const themeTotals = {};
    lossData.forEach(item => {
        if (themeTotals[item.theme]) {
            themeTotals[item.theme] += item.total;
        } else {
            themeTotals[item.theme] = item.total;
        }
    });

    // Извлекаем темы и их суммы для графика
    const themes = Object.keys(themeTotals);
    const totals = Object.values(themeTotals);

    // Создаем график
    const ctx = document.getElementById('lossChart').getContext('2d');
    const lossChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: themes,
            datasets: [{
                label: 'Total Loss by Theme',
                data: totals,
                backgroundColor: 'rgba(255, 99, 132, 0.2)', 
                borderColor: 'rgba(255, 99, 132, 1)',
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
