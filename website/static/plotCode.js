document.addEventListener("DOMContentLoaded", function() {
    var trace1 = {
        x: [0, 1, 2, 3, 4, 5],
        y: [Math.floor(Math.random()*1000), Math.floor(Math.random()*1000), Math.floor(Math.random()*1000), 
            Math.floor(Math.random()*1000), Math.floor(Math.random()*1000), Math.floor(Math.random()*1000)],
        mode: 'lines',
        name: 'testing',
        line: {
          dash: 'dashdot',
          width: 4
        }
      };
      
      var trace2 = {
        x: [0, 1, 2, 3, 4, 5],
        y: [Math.floor(Math.random()*1000), Math.floor(Math.random()*1000), Math.floor(Math.random()*1000),
            Math.floor(Math.random()*1000), Math.floor(Math.random()*1000), Math.floor(Math.random()*1000)],
        mode: 'lines',
        name: 'dashdot',
        line: {
          dash: 'dashdot',
          width: 4
        }
      };
      
 
      var data = [trace1];
      
      var layout = {
        title: 'Line Dash',
        xaxis: {
          range: [0, 5],
          autorange: false
        },
        yaxis: {
          range: [0, 1000],
          autorange: true
        },
        legend: {
          y: 0.5,
          traceorder: 'reversed',
          font: {
            size: 16
          }
        }
      };
      
      Plotly.newPlot('plot', data, layout);
      
});