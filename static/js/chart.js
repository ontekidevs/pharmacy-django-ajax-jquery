
//Charts
// Data Picker Initialization
    $('.datepicker').pickadate();

// Small chart
$(function () {
    $('.min-chart#chart-sales').easyPieChart({
    barColor: "#4caf50",
    onStep: function (from, to, percent) {
        $(this.el).find('.percent').text(Math.round(percent));
    }
    });
});

//Main chart
var ctxL = document.getElementById("lineChart-main").getContext('2d');
var myLineChart = new Chart(ctxL, {
    type: 'line',
    data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [{
        label: "My First dataset",
        fillColor: "#fff",
        backgroundColor: 'rgba(255, 255, 255, .3)',
        borderColor: 'rgba(255, 255, 255, .9)',
        data: [0, 10, 5, 2, 20, 30, 45],
    }]
    },
    options: {
    legend: {
        labels: {
        fontColor: "#fff",
        }
    },
    scales: {
        xAxes: [{
        gridLines: {
            display: true,
            color: "rgba(255,255,255,.25)"
        },
        ticks: {
            fontColor: "#fff",
        },
        }],
        yAxes: [{
        display: true,
        gridLines: {
            display: true,
            color: "rgba(255,255,255,.25)"
        },
        ticks: {
            fontColor: "#fff",
        },
        }],
    }
    }
});

