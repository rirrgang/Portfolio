// Use JavaScript to add the 'odd' class to the odd occurrences of education-symbol and contact-symbol
function updateOddHexagonSymbols() {
  const symbols = document.querySelectorAll(".education-symbol, .contact-symbol", "experience-symbol");

  symbols.forEach((symbol, index) => {
    if (index % 2 !== 0) {
      symbol.classList.add("odd");
    }
  });
}

updateOddHexagonSymbols();
