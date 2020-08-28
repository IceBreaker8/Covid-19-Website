window.onload = graphShowcase


function background(color) {
    var border = new Array();
    for (let i = 0; i < dayNumbers; i++) {
        border.push(color);
    }
    return border;
}


function graphShowcase() {

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: dates,
                datasets: [
                    {
                        label: "Total Deaths",
                        data:
                        deaths,
                        backgroundColor: background("#B22222"),
                        borderWidth: 1
                    },
                    {
                        label: "Total Recoveries",
                        data:
                        recov,
                        backgroundColor: background("#228B22"),
                        borderWidth: 1
                    },
                    {
                        label: "Total cases",
                        data:
                        cases,
                        backgroundColor: background("#4682B4"),
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: false
                        }
                    }]
                }
            }
        })
    ;
    calculNumber();
}

function calculNumber() {
    nums = new Array();
    percentages = new Array();
    var statArray = cases;
    var len = statArray.length;
    for (var i = 1; i < len; i++) {
        let s = statArray[len - i] - statArray[len - 1 - i];
        nums.push(s);
        percentages.push(s / statArray[len - i] * 100);
    }
    var avg = 0;
    var percentage = 0;
    for (var i = 0; i < nums.length; i++) {
        avg += nums[i];
        percentage += percentages[i];
    }
    avg = (avg / nums.length).toFixed(2);
    percentage = (percentage / percentages.length).toFixed(2);

    //injection of HTML
    document.getElementById("styled").style.display = "block";
    document.getElementById("styled").innerHTML =
        `<span class=\"a\">Average Daily Case Increase of</span>\n
                       <span class=\"b\">${avg}</span>
                       (<span class=\"c\">${percentage}%</span>)`;

}



