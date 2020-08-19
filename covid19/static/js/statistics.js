

var searchBox = document.getElementById("searchbox")
var c = document.getElementById("myDropdown");
//search on click choice ====================================================


//============================================================================

shown = false;

function onInputWord() {
    c.style.display = "block";

    //clearing html
    c.innerHTML = "";

    //modifying c innerHTML
    for (i = 0; i < countryList.length; i++) {
        var s = countryList[i];
        if (s.toLowerCase().startsWith(searchBox.value.toLowerCase())) {
            c.innerHTML += `<a href='#' name="${s}"
                        onclick="choiceFunc(name)">${s}</a>`;
        }

    }

    if (!shown) {
        document.getElementById("myDropdown").classList.toggle("show");
        shown = true;
    }
}


function onSearchBoxClick() {
    if (searchBox.value.toString().length != 0) {
        c.style.display = "block";
    } else {
        c.style.display = "none";
    }

    //clearing html
    c.innerHTML = "";
    searchBox = document.getElementById("searchbox")

    //modifying c innerHTML
    for (i = 0; i < countryList.length; i++) {
        var s = countryList[i];
        if (s.toLowerCase().startsWith(searchBox.value.toLowerCase()) &&
            searchBox.value != "") {
            c.innerHTML += `<a href='#' name="${s}"
                        onclick="choiceFunc(name)">${s}</a>`;
        }


    }

    if (!shown) {
        document.getElementById("myDropdown").classList.toggle("show");
        shown = true;
    }
}

function exitInputBox() {

    return false;
}

function choiceFunc(countryName) {
    searchBox.value = countryName;
    //modifying css
    c.innerHTML = "";
    c.style.display = "none";
    //TODO database
    graphShowcase(countryName);

    return false;
}


function lookForCountry(allData, string) {
    for (var i = 0; i < allData.length; i++) {
        if (allData[i][0][1] == string) {
            displayChart(allData[i]);
            return;
        }
    }

}


function displayChart(countryData) {
    ///////////// get dates /////////////////////////////////////
    dateArray = new Array();
    for (var i = 0; i < countryData.length; i++) {
        dateArray.push(countryData[i][0]);
    }
    dateArray.reverse();

    //////////// get stats //////////////////////
    statArray = new Array();
    for (var i = 0; i < countryData.length; i++) {
        statArray.push(countryData[i][2]);
    }
    statArray.reverse();

}

var myChart;

function graphShowcase(string) {
    lookForCountry(allData, string);
    var ctx = document.getElementById('myChart').getContext('2d');
    if (myChart != undefined) {
        myChart.destroy();
    }
    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: dateArray,
            datasets: [{
                label: string + "'s Coronavirus Cases reported the last "
                    + dates + " days",
                data
:
    statArray,
        backgroundColor
:
    [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
    ],
        borderColor
:
    [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
    ],
        borderWidth
:
    1
}]
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



