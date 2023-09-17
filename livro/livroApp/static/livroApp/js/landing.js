window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    var navbar = document.getElementById("myNavbar");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        navbar.classList.add("navbar-shadow"); // Add the shadow class
    } else {
        navbar.classList.remove("navbar-shadow"); // Remove the shadow class
    }
}