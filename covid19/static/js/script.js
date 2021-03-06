function Get(yourUrl) {
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET", yourUrl, false);
    Httpreq.send(null);
    return Httpreq.responseText;
}

function DrawCircle(color, state) {
    group1.clearLayers()
    switch (state) {
        case "TC":
            var str_ = "cases";
            break;
        case "CPM":
            var str_ = "casesPerOneMillion";
            break;
        case "Rec":
            var str_ = "recovered";
            break;
        case "Ds":
            var str_ = "deaths";
            break;
        case "FR":
            var str_ = "cases";
            var state = "recovered";
            break;
        case "DPM":
            var str_ = "deathsPerOneMillion";
            break;
        case "Act":
            var str_ = "sick";
            break;
        case "name":
            var str_ = "cases";
            break;
        default:
            var str_ = "cases";

    }
    for (var i = 0; i < json_obj.length; i++) {
        let lat = json_obj[i]["countryInfo"]["lat"];
        let long = json_obj[i]["countryInfo"]["long"];
        let flag_url = json_obj[i]["countryInfo"]["flag"];
        let cases = json_obj[i][str_]
        let iso = json_obj[i]["countryInfo"]["iso3"];
        let _id = json_obj[i]["countryInfo"]["_id"];
        let country = json_obj[i]["country"];
        let todayCases = json_obj[i]["todayCases"];
        let Recoveries = json_obj[i]["recovered"];
        let Deaths = json_obj[i]["deaths"]
        if (cases > 1000000) {
            radius = cases / 5;
        } else if (cases < 1000000 && cases > 500000) {
            radius = cases / 1;
        } else if (cases < 500000 && cases > 100000) {
            radius = cases;
        } else if (cases < 100000 && cases > 50000) {
            radius = cases;
        } else if (cases < 50000 && cases > 25000) {
            radius = cases * 5;
        } else if (cases < 25000 && cases > 10000) {
            radius = cases * 8;
        } else if (cases < 10000) {
            radius = cases * 25;
        } else if (cases < 5000) {
            radius = cases * 100;
        } else if (cases < 1000) {
            radius = cases * 100000;
        }
        switch (color) {
            case "red": {
                var circle = L.circle([lat, long], {
                    color: "#ff416c",
                    fillColor: "#f03",
                    fillOpacity: 0.4,
                    radius: radius,
                    color: "#ff416c",
                    strokeopacity: 0.5,
                    strokewidth: 1,
                    weight: 0,
                }).addTo(group1);
                var col = '#f03';
                break;
            }
            case "green": {
                console.log("green called");
                var circle = L.circle([lat, long], {
                    color: "#00FA9A",
                    fillColor: "#00FA9A",
                    fillOpacity: 0.6,
                    radius: radius,
                    color: "#00FA9A",
                    strokeopacity: 0.5,
                    strokewidth: 1,
                    weight: 1,
                }).addTo(group1);
                var col = "#00FA9A";
                break;

            }
            case "purple": {
                var circle = L.circle([lat, long], {
                    color: "#9370DB",
                    fillColor: "#9370DB",
                    fillOpacity: 0.6,
                    radius: radius,
                    color: "#9370DB",
                    strokeopacity: 0.5,
                    strokewidth: 1,
                    weight: 1,
                }).addTo(group1);
                var col = '#9370DB';
                break;

            }
        }
        var popup2 = L.popup({
            offset: L.point(20, 40)
        }).setContent('<div class="map-tooltip Tooltip main-map"><img src=' + flag_url + '><div class="map-tooltip-title"><div>' + country + '</div></div><div class="map-tooltip-new">+' + todayCases + '</div><div class="map-tooltip-line infected"><span>' + cases + '</span><span>Total cases</span></div><div class="map-tooltip-line recovered"><span>' + Recoveries + '</span><span>Recoveries</span></div><div class="map-tooltip-line dead"><span>' + Deaths + '</span><span>Deaths</span></div></div>');
        circle.bindPopup(popup2);
        circle.on("mouseover", function (evt) {
            this.openPopup([lat, long]);
            this.setStyle({
                fillColor: "yellow",
            });
        });
        circle.on('mouseout   ', function (evt) {
            this.setStyle({
                fillColor: col,
            });
        });

        circle.on('click', function (evt) {
            window.location.href = 'statistics/'.concat(_id);
        })

    }
    mymap.addLayer(group1);

}

function fillred() {
    var cc = document.getElementsByTagName("path");
    for (i = 0; i < cc.length; i++) {
        cc[i].classList.add('MyClass')
        cc[i].style.fillOpacity = "0.5";
        cc[i].style.strokewidth = "2";
    }
}

function mff() {
    cont.innerHTML = "";
    for (let i = 0; i < json_obj.length; i++) {
        let flag_url = json_obj[i]["countryInfo"]["flag"];
        let cases = json_obj[i]["cases"]
        let name = json_obj[i].country
        document.getElementsByClassName("map-sidebar-sort")[0].innerHTML = "Total Cases";
        cont.innerHTML += `<div class="map-sidebar-section-item" id="` + i + `>
         <div class="map-sidebar-section-item-img"><img class="flag-img" src=` + flag_url + `></div>
        <div class="map-sidebar-section-item-details">
          <div class="map-sidebar-section-item-title" id="label">` + name + `</div>
    </div>
     <div class="map-sidebar-section-item-nb infected">` + cases + `</div>
    </div> `;
    }
    var bug = 0;
    for (let i = 0; i < json_obj.length; i++) {
        $("#" + i).on("click", function () {
            let lat = json_obj[this.id]["countryInfo"]["lat"];
            console.log(lat);
            let long = json_obj[this.id]["countryInfo"]["long"];
            mymap.setView([lat, long]);
        })
    }
}

function mf(jsonfile, SortBy) {
    cont.innerHTML = "";
    var str_;
    var state;
    switch (SortBy) {
        case "TC":
            str_ = "cases";
            state = "infected";
            break;
        case "CPM":
            str_ = "casesPerOneMillion";
            state = "infected";

            break;
        case "Rec":
            str_ = "recovered";
            state = "recovered";
            break;
        case "Ds":
            str_ = "deaths";
            state = "dead";
            break;
        case "FR":
            str_ = "cases";
            state = "recovered";
            break;
        case "DPM":
            str_ = "deathsPerOneMillion";
            state = "dead";
            break;
        case "Act":
            str_ = "sick";
            break;
        case "name":
            str_ = "cases";
            state = "infected";
            break;
        default:
            str_ = "cases";

    }
    for (var i = 0; i < jsonfile.length; i++) {
        let flag_url = jsonfile[i]["countryInfo"]["flag"];
        let name = jsonfile[i].country
        let Report = jsonfile[i][str_]
        console.log(state);
        cont.innerHTML += `<div class="map-sidebar-section-item" id=` + i + ` >
         <div class="map-sidebar-section-item-img"><img class="flag-img" src=` + flag_url + `></div>
        <div class="map-sidebar-section-item-details">
          <div class="map-sidebar-section-item-title">` + name + `</div>
    </div>
     <div class="map-sidebar-section-item-nb `.concat(state) + `">` + Report + `</div>
    </div> `;
        //$(".map-sidebar-section-item").on("click",function(){console.log("Bitch yes please");})

    }
    console.log(jsonfile);
    for (let i = 0; i < jsonfile.length; i++) {
        $("#" + i).on("click", function () {
            let lat = jsonfile[this.id]["countryInfo"]["lat"];
            console.log(lat);
            let long = jsonfile[this.id]["countryInfo"]["long"];
            mymap.setView([lat, long]);
        })
    }

    //$(".map-sidebar-section-item").on("click",function(){console.log("Bitch yes please");})
    //$(".map-sidebar-section-content").on("click",$("div.map-sidebar-section-item"),function(){console.log("Bitch noo please");})
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}


OnLoad();

function OnLoad() {
    let s = document.getElementById("vanish");
    let string = window.location.href;
    if (string.toLowerCase().includes("statistics")
        || string.toLowerCase().includes("overview")) {
        s.style.display = "inline";
    } else {
        s.style.display = "none";
    }


}

