new Chart(document.getElementById("chart"), {
    type: 'line',
    data: {
        labels: xAxis,
        datasets: [{
            data: yAxisConfirmed,
            label: "Total Cases",
            borderColor: "#0075bd",
            fill: false
        }, {
            data: yAxisDeaths,
            label: "Total Deaths",
            borderColor: "#ef0c0c",
            fill: false
        }, {
            data: yAxisRecov,
            label: "Total Recovered",
            borderColor: "#0fba34",
            fill: false
        }
        ]
    },
    options: {
        title: {
            display: true,
            text: 'Coronavirus Worldwide Dashboard for the last ' + xAxisWidth + ' days'
        }
    }
});
