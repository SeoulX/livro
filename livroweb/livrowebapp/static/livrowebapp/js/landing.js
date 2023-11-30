document.addEventListener('DOMContentLoaded', function () {
    function openPopup(url) {
        fetch(url)
        .then(response => response.text())
        .then(data => {
            var popupContainer = document.getElementById('popup-container');
            popupContainer.innerHTML = data;
            popupContainer.style.display = 'flex';
            popupContainer.classList.add('overlay');  // Add the overlay class
        })
        .catch(error => console.error('Error fetching content:', error));
}



    document.getElementById('login-button').addEventListener('click', function () {
        openPopup('/signin/');
    });

    document.getElementById('signup-button').addEventListener('click', function () {
        openPopup('/signup/');
    });

    window.addEventListener('popstate', function (event) {
        closePopup();
    });

});

function closeSignIn() {
    document.querySelector('.wrap').style.display = 'none';
    removeOverlay();
}

document.addEventListener('DOMContentLoaded', function () {
    var closeButton = document.querySelector('.closebutton');
    if (closeButton) {
        closeButton.addEventListener('click', closeSignIn);
    }
});

function closeSignUp() {
    document.querySelector('.popup').style.display = 'none';
    removeOverlay();
}

document.addEventListener('DOMContentLoaded', function () {
    var closeButton = document.querySelector('.close-btn');
    if (closeButton) {
        closeButton.addEventListener('click', closeSignUp);
    }
});

function removeOverlay() {
    var popupContainer = document.getElementById('popup-container');
    popupContainer.innerHTML = '';  // Clear the content when closing
    popupContainer.style.display = 'none';
    popupContainer.classList.remove('overlay');  // Remove the overlay class
}