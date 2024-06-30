// Function to make navigation nav-item active
function makeNavItemActive(targetId) {
  const navigationItems = document.querySelectorAll(".navbar-nav .nav-item");

  navigationItems.forEach((item) => {
    const itemLink = item.querySelector("a");
    if (itemLink.getAttribute("href") === targetId) {
      item.classList.add("active");
    } else {
      item.classList.remove("active");
    }
  });
}

function isSectionInViewport(section) {
  const rect = section.getBoundingClientRect();
  const windowHeight = window.innerHeight;

  return rect.top <= windowHeight * 0.5 && rect.bottom >= windowHeight * 0.5;
}

// Add 'active' class to navigation items when their corresponding sections are in the viewport
function toggleActiveState() {
  const sections = document.querySelectorAll("section");

  sections.forEach((section) => {
    const targetId = "#" + section.getAttribute("id");
    const navigationItems = document.querySelectorAll(".navbar-nav .nav-item");

    if (isSectionInViewport(section)) {
      makeNavItemActive(targetId);
    } else {
      navigationItems.forEach((item) => {
        const itemLink = item.querySelector("a");
        if (itemLink.getAttribute("href") === targetId) {
          item.classList.remove("active");
        }
      });
    }
  });
}

// Smooth scroll to anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    // Get the target element's ID from the href attribute
    const targetId = this.getAttribute("href");

    // Get the target element by its ID
    const targetElement = document.querySelector(targetId);

    if (targetElement) {
      // Calculate the scroll position, accounting for the fixed navigation bar height
      const navbarHeight = document.querySelector(".navbar").offsetHeight;
      const scrollToPosition = targetElement.offsetTop - navbarHeight;

      // Scroll smoothly to the target element
      window.scrollTo({
        top: scrollToPosition,
        behavior: "smooth",
      });

      // close the nav menu if it is opened:
      setTimeout(() => {
        const navbarToggler = document.querySelector(".navbar-toggler");
        const navbarCollapse = document.querySelector(".navbar-collapse");

        if (navbarCollapse.classList.contains("show")) {
          //navbarCollapse.classList.remove("show");
          navbarToggler.click();
        }
      }, 300);

      // Make the clicked navigation item active
      makeNavItemActive(targetId);
    }
  });
});

// Toggle active state on scroll and resize
function handleScrollAndResize() {
  toggleActiveState();
}

window.addEventListener("scroll", handleScrollAndResize);
window.addEventListener("resize", handleScrollAndResize);
