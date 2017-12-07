$("#pick").click(function() {
  $.ajax("/pick", { method: "POST" });
  draw({ 4: 0.2, 6: 0.2, 8: 0.2, 12: 0.2, 20: 0.2 });
});

$("#roll").click(function() {
  $.ajax("/roll", {
    method: "POST",
    success: function(posterior) {
      console.log(posterior);
      draw(posterior);
    }
  });
});

function draw(posterior) {
  if (!posterior) {
    y = [0.2, 0.2, 0.2, 0.2, 0.2];
  } else {
    var { 4: a, 6: b, 8: c, 12: d, 20: e } = posterior;
    y = [a, b, c, d, e];
  }

  var data = [
    {
      x: ["d4", "d6", "d8", "d12", "d20"],
      y: y,
      type: "bar"
    }
  ];

  var layout = {
    yaxis: { range: [0, 1] }
  };

  Plotly.newPlot("histogram", data, layout);
}

draw();
