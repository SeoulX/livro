
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    var navbar = document.getElementById("myNavbar");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        navbar.classList.add("navbar-shadow"); // Add the shadow class
    } else {
        navbar.classList.remove("navbar-shadow"); // Remove the shadow class
    }
}
const searchNav = document.getElementById("searchNav");
const closeBtn = document.getElementById("closeBtn");
const searchIcon = document.querySelector(".search-icon");

// Open the search navigation
searchIcon.addEventListener("click", () => {
    searchNav.style.width = "25%"; // Adjust the width as needed
});

// Close the search navigation
closeBtn.addEventListener("click", () => {
    searchNav.style.width = "0";
});