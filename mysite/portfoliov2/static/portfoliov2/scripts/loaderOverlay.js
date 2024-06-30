document.addEventListener("DOMContentLoaded", function () {
  var loaderOverlay = document.getElementById("loader");
  var content = document.querySelector(".content");
  var elements = document.querySelectorAll("#text-animation");

  // Function to hide the loader
  function hideLoader() {
    loaderOverlay.classList.add("hide-overlay");
    content.classList.add("loaded");
  }

  // Function to start the typewriter animation
  function startTypewriterAnimation() {
    elements.forEach(function (element) {
      var text = element.textContent;
      element.textContent = "";
      var options = {
        strings: [text],
        typeSpeed: 50,
        showCursor: false,
      };

      var typed = new Typed(element, options);
    });
  }

  // Counter to track loading status
  var loadingCounter = 1;

  // Function to check if both loader and content are loaded
  function checkLoadingComplete() {
    loadingCounter--;
    //console.log("loadingCounter: " + loadingCounter);
    if (loadingCounter === 0) {
      hideLoader();
      startTypewriterAnimation();
      animateOnScroll();
    }
  }

  function animateOnScroll() {
    var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    var aosElements = document.querySelectorAll("[data-aos-delay]");

    if (isMobile) {
      aosElements.forEach(function (element) {
        element.setAttribute("data-aos-delay", 0);
      });
    }

    AOS.init();
  }

  // Check if video player exists and add event listener for loadedmetadata if available
  // var videoPlayer = document.getElementById('videoPlayer');
  // if (videoPlayer) {
  //     loadingCounter += 2; // Increment the loading counter since video player is present
  //     videoPlayer.addEventListener('loadeddata', checkLoadingComplete);
  //     videoPlayer.addEventListener('canplaythrough', checkLoadingComplete);
  // } else {
  //     checkLoadingComplete(); // Call checkLoadingComplete directly if there is no video player
  // }

  // Add event listener for DOMContentLoaded to check if content is loaded
  window.addEventListener("DOMContentLoaded", checkLoadingComplete);
});
