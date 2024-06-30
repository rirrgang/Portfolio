document.addEventListener("DOMContentLoaded", function () {
  var progressBarElements = document.querySelectorAll(".custom-progress-bar");
  var controller = new ScrollMagic.Controller();

  progressBarElements.forEach(function (element) {
    //get options from dataset if available
    var type = element.dataset.type || "line";
    var color = element.dataset.color || "#000000";
    var trailColor = element.dataset.trailcolor || "#aeaeae";
    var trailWidth = element.dataset.trailwidth || 2;
    var progress = parseFloat(element.dataset.progress) || 1;
    var strokeWidth = parseFloat(element.dataset.strokewidth) || 1;
    var duration = parseFloat(element.dataset.duration) || 1000;
    var easing = element.dataset.easing || "easeOut";

    var defaultOptions = {
      color: color,
      strokeWidth: strokeWidth,
      trailColor: trailColor,
      trailWidth: trailWidth,
      duration: duration,
      easing: easing,
      text: {
        style: {
          // Other styles...
          color: "#ffffff",
          fontSize: "1.5rem",
          fontWeight: "bold",
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
        },
      },
      step: function (state, elem) {
        var value = Math.round(elem.value() * 100);
        if (value < 0) {
          elem.setText("0%");
        } else {
          elem.setText(value + "%");
        }
      },
    };

    var progressBar;
    var type = element.dataset.type || "line";

    switch (type) {
      case "line":
        progressBar = new ProgressBar.Line(element, {
          ...defaultOptions,
        });
        break;
      case "circle":
        progressBar = new ProgressBar.Circle(element, {
          ...defaultOptions,
        });
        break;
      case "semi-circle":
        progressBar = new ProgressBar.SemiCircle(element, {
          ...defaultOptions,
        });
        break;
      case "path":
        progressBar = new ProgressBar.Circle(element, {
          ...defaultOptions,
        });
        customPath = element.dataset.custompath || null;
        if (customPath) {
          element.querySelectorAll("path").forEach(function (path, index) {
            path.setAttribute("d", customPath);
            // Calculate the total length of the path
            const totalLength = path.getTotalLength();

            // Check if it's the second path element (index 1)
            if (index === 1) {
              // Set the total length as the value of stroke-dashoffset and stroke-dasharray
              path.style.strokeDashoffset = totalLength;
              path.style.strokeDasharray = totalLength;
            }
          });
        }
        break;
      default:
        progressBar = new ProgressBar.line(element, {
          ...defaultOptions,
        });
        break;
    }

    // Scene for onEnter
    var enterScene = new ScrollMagic.Scene({
      triggerElement: element,
      triggerHook: 0.9, // show, when scrolled 10% into view
      duration: "100%", // hide 10% before exiting view (80% + 10% from bottom)
      offset: 100, // move trigger to center of element
    })
      .addTo(controller)
      .on("enter", function () {
        progressBar.animate(progress);
        //console.log("entering");
      })
      .on("leave", function () {
        progressBar.animate(0);
        // progressBar.set(0);
        //console.log("leaving");
      });
  });
});
