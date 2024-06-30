document.addEventListener("DOMContentLoaded", function () {
  var swipeIcon = document.getElementById("swipe-icon");
  var swipeButton = document.getElementById("swipe-button");
  var swipeAnchor = document.getElementById("swipe-anchor");

  if (swipeIcon && swipeButton && swipeAnchor) {
    var anchorWidth = swipeButton.offsetWidth;
    var iconWidth = swipeIcon.offsetWidth;
    var maxSwipeDistance = anchorWidth - iconWidth;
    var halfAnchorWidth = anchorWidth / 2;

    var startX = 0;
    var endX = 0;
    var isSwiping = false;

    swipeButton.addEventListener("mouseup", function () {
      if (!isSwiping) swipeAnchor.click();
    });

    swipeButton.addEventListener("mouseover", function () {
      swipeIcon.style.animationName = "none";
    });

    swipeButton.addEventListener("mouseout", function () {
      swipeIcon.style.animationName = "swipe-jiggle-anim";
    });

    swipeIcon.addEventListener("mousedown", function (event) {
      startX = event.clientX;
      isSwiping = true;
    });

    window.addEventListener("mousemove", function (event) {
      if (isSwiping) {
        endX = event.clientX;
        var swipeDistance = endX - startX;
        var translatedDistance = Math.min(Math.max(0, swipeDistance), maxSwipeDistance);
        swipeIcon.style.transform = `translateX(${translatedDistance}px)`;
      }
    });

    window.addEventListener("mouseup", function (event) {
      if (isSwiping) {
        handleSwipe();
        isSwiping = false;
      }
    });

    swipeIcon.addEventListener("touchstart", function (event) {
      swipeIcon.style.animationName = "none";
      startX = event.changedTouches[0].screenX;
    });

    swipeIcon.addEventListener("touchmove", function (event) {
      endX = event.changedTouches[0].screenX;
      var swipeDistance = endX - startX;
      var translatedDistance = Math.min(Math.max(0, swipeDistance), maxSwipeDistance);
      swipeIcon.style.transform = `translateX(${translatedDistance}px)`;
    });

    swipeIcon.addEventListener("touchend", function (event) {
      handleSwipe();
      swipeIcon.style.animationName = "swipe-jiggle-anim";
    });

    function handleSwipe() {
      var swipeDistance = endX - startX;
      var threshold = 50;

      //add transition for smooth translation of icon:
      swipeIcon.style.transition = "0.3s ease-in-out";

      //if swiped to the right do:
      if (Math.abs(swipeDistance) > halfAnchorWidth - threshold) {
        var targetDistance = swipeDistance > 0 ? maxSwipeDistance : 0;
        swipeIcon.style.transform = `translateX(${targetDistance}px) rotate(90deg)`;

        setTimeout(function () {
          swipeAnchor.click();
        }, 300);
      } else {
        swipeIcon.style.transform = "translateX(0) rotate(360deg)";
      }

      //reset icon position after 600ms
      setTimeout(function () {
        swipeIcon.style.transform = "translateX(0) rotate(360deg)";
      }, 600);

      //reset transition for smooth translation of icon after 900ms
      setTimeout(function () {
        swipeIcon.style.transition = "none";
      }, 900);
    }
  }
});
