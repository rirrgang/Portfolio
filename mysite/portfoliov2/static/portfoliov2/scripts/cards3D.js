const cards = document.querySelectorAll(".card-3d-rotation");

add3DEffect(cards);

function add3DEffect(cards) {
  cards.forEach(function (card) {
    card.addEventListener("mousemove", rotate);
    card.addEventListener("mouseleave", clearRotate);

    const cardButton = card.querySelectorAll(".btn");
    cardButton.forEach(function (btn) {
      btn.addEventListener("mousemove", function (e) {
        clearRotate.call(card, e);
      });
      btn.addEventListener("mouseleave", function (e) {
        clearRotate.call(card, e);
      });
    });
  });
}

function rotate(e) {
  // Check if the event target is a button
  if (e.target.classList.contains("btn")) {
    return;
  }

  const force = 15;
  const cardItem = this.querySelector(".card-item");
  const rect = cardItem.getBoundingClientRect();
  const centerX = e.clientX - rect.x - rect.width / 2;
  const centerY = e.clientY - rect.y - rect.height / 2;
  const rotateX = -(e.offsetY - cardItem.offsetHeight / 2) / force;
  const rotateY = (e.offsetX - cardItem.offsetWidth / 2) / force;

  gsap.to(cardItem, {
    rotationX: rotateX,
    rotationY: rotateY,
    duration: 1,
    ease: "sine.easeInOut",
  });

  var gradient = `
            radial-gradient(
            circle at
            ${centerX * 2 + rect.width / 2}px
            ${centerY * 2 + rect.height / 2}px,  
            #ffffff55,
            #0000000f
            )
        `;
  var gradient2 = `
            radial-gradient(
            circle at
            ${centerX * 2 + rect.width / 2}px
            ${centerY * 2 + rect.height / 2}px,  
            #ffa600d6,
            #0000000f
            )
        `;
  cardItem.querySelector(".card-3d-glow").style.backgroundImage = gradient;

  if (isProjectCard(cardItem)) {
    cardItem.querySelector(".card-body").style.background = "#f59b0bbf";
  }
}

function isProjectCard(cardItem) {
  if (cardItem && cardItem.parentNode && cardItem.parentNode.parentNode) {
    return cardItem.parentNode.parentNode.classList.contains("project-card");
  }
  return false;
}

function clearRotate(e) {
  const cardItem = this.querySelector(".card-item");
  cardItem.querySelector(".card-3d-glow").style.backgroundImage = "";

  gsap.to(cardItem, {
    rotationX: 0,
    rotationY: 0,
    duration: 1,
    ease: "sine.easeInOut",
  });
  // cardItem.style.boxShadow = "0 0 0px rgb(0, 0, 0)";

  if (isProjectCard(cardItem)) {
    cardItem.querySelector(".card-body").style.background = "#ffffff00";
  }
}
