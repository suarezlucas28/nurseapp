var config = {
  type: 'line',
  data: {
      labels: labels,
      datasets: [{
          label: 'blood pressure',
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderWidth: 1,
          data: data1,
          fill: false,
      }, {
          label: 'heart rate',
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderWidth: 1,
          data: data2,
          fill: false,
      }]
  },
  options: {
      responsive: true,
      title: {
          display: true,
          text: 'History Values'
      },
      scales: {
          xAxes: [{
              display: true,
              scaleLabel: {
                  display: true,
                  labelString: 'Days'
              }
          }],
          yAxes: [{
              display: true,
              scaleLabel: {
                  display: true,
                  labelString: 'Value'
              }
          }]
      }
  }
};

window.onload = function() {
    var ctx = document.getElementById('canvas').getContext('2d');
    window.myLine = new Chart(ctx, config);
};