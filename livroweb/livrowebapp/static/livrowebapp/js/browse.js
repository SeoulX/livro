document.addEventListener('DOMContentLoaded', function () {
    function openPopup(url) {
        fetch(url)
        .then(response => response.text())
        .then(data => {
            var popupContainer = document.getElementById('popup-container');
            popupContainer.innerHTML = data;
            popupContainer.style.display = 'flex';
            popupContainer.classList.add('overlay');  // Add the overlay class

            if(url == '/signup/'){
                let password = document.getElementById ("password");
                let confirmpassword = document.getElementById ("confirmpassword");
                let showpassword = document.getElementById ("showpassword");
            
                showpassword.onclick = function (){
                    if(password.type == "password") {
                        password.type = "text";
                        confirmpassword.type = "text"
                    }else{
                        password.type = "password";
                        confirmpassword.type = "password"
                    }
                
                    password.classList.toggle("show-password");
                    confirmpassword.classList.toggle("show-password");
            };}
                
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

document.addEventListener('DOMContentLoaded', function () {
    function openPopup(url) {
        fetch(url)
        .then(response => response.text())
        .then(data => {
            var popupContainer = document.getElementById('popup-container');
            popupContainer.innerHTML = data;
            popupContainer.style.display = 'flex';
            popupContainer.classList.add('overlay');  // Add the overlay class

            if(url == '/signup/'){
                let password = document.getElementById ("password");
                let confirmpassword = document.getElementById ("confirmpassword");
                let showpassword = document.getElementById ("showpassword");

                showpassword.onclick = function (){
                    if(password.type == "password") {
                        password.type = "text";
                        confirmpassword.type = "text"
                    }else{
                        password.type = "password";
                        confirmpassword.type = "password"
                    }

                    password.classList.toggle("show-password");
                    confirmpassword.classList.toggle("show-password");
            };}
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

var gen1 = document.getElementById('g1');
var gen2 = document.getElementById('g2');
var gen3 = document.getElementById('g3');
var gen4 = document.getElementById('g4');
var gen5 = document.getElementById('g5');
var gen6 = document.getElementById('g6');
var gen7 = document.getElementById('g7');
var gen8 = document.getElementById('g8');
var gen9 = document.getElementById('g9');
var alldiv = document.getElementsByClassName('genrebox');
var display = 0;

const actbtn = document.getElementById('actionbtn');
const fanbtn = document.getElementById('fantasybtn');
const youngbtn = document.getElementById('youngbtn');
const combtn = document.getElementById('comedybtn');
const rombtn = document.getElementById('romancebtn');
const nonfbtn = document.getElementById('nonficbtn');
const scifbtn = document.getElementById('scifibtn');
const horbtn = document.getElementById('horrorbtn');

actbtn.addEventListener('click', () => {
    display = 1;
    updateGenreDisplay();
});

fanbtn.addEventListener('click', () => {
    display = 2;
    updateGenreDisplay();
});

youngbtn.addEventListener('click', () => {
    display = 3;
    updateGenreDisplay();
});

combtn.addEventListener('click', () => {
    display = 4;
    updateGenreDisplay();
});

rombtn.addEventListener('click', () => {
    display = 5;
    updateGenreDisplay();
});

nonfbtn.addEventListener('click', () => {
    display = 6;
    updateGenreDisplay();
});

scifbtn.addEventListener('click', () => {
    display = 7;
    updateGenreDisplay();
});

horbtn.addEventListener('click', () => {
    display = 8;
    updateGenreDisplay();
});

function updateGenreDisplay() {
    if (display === 1) {
        gen1.style.display = 'none';
        gen2.style.display = 'block';
        gen3.style.display = 'none';
        gen4.style.display = 'none';
        gen5.style.display = 'none';
        gen6.style.display = 'none';
        gen7.style.display = 'none';
        gen8.style.display = 'none';
        gen9.style.display = 'none';
    } else if (display === 2) {
        gen1.style.display = 'none';
        gen2.style.display = 'none';
        gen3.style.display = 'block';
        gen4.style.display = 'none';
        gen5.style.display = 'none';
        gen6.style.display = 'none';
        gen7.style.display = 'none';
        gen8.style.display = 'none';
        gen9.style.display = 'none';
    } else if (display === 3) {
        gen1.style.display = 'none';
        gen2.style.display = 'none';
        gen3.style.display = 'none';
        gen4.style.display = 'block';
        gen5.style.display = 'none';
        gen6.style.display = 'none';
        gen7.style.display = 'none';
        gen8.style.display = 'none';
        gen9.style.display = 'none';
    } else if (display === 4) {
        gen1.style.display = 'none';
        gen2.style.display = 'none';
        gen3.style.display = 'none';
        gen4.style.display = 'none';
        gen5.style.display = 'block';
        gen6.style.display = 'none';
        gen7.style.display = 'none';
        gen8.style.display = 'none';
        gen9.style.display = 'none';
    } else if (display === 5) {
        gen1.style.display = 'none';
        gen2.style.display = 'none';
        gen3.style.display = 'none';
        gen4.style.display = 'none';
        gen5.style.display = 'none';
        gen6.style.display = 'block';
        gen7.style.display = 'none';
        gen8.style.display = 'none';
        gen9.style.display = 'none';
    } else if (display === 6) {
        gen1.style.display = 'none';
        gen2.style.display = 'none';
        gen3.style.display = 'none';
        gen4.style.display = 'none';
        gen5.style.display = 'none';
        gen6.style.display = 'none';
        gen7.style.display = 'block';
        gen8.style.display = 'none';
        gen9.style.display = 'none';
    } else if (display === 7) {
        gen1.style.display = 'none';
        gen2.style.display = 'none';
        gen3.style.display = 'none';
        gen4.style.display = 'none';
        gen5.style.display = 'none';
        gen6.style.display = 'none';
        gen7.style.display = 'none';
        gen8.style.display = 'block';
        gen9.style.display = 'none';
    } else if (display === 8) {
        gen1.style.display = 'none';
        gen2.style.display = 'none';
        gen3.style.display = 'none';
        gen4.style.display = 'none';
        gen5.style.display = 'none';
        gen6.style.display = 'none';
        gen7.style.display = 'none';
        gen8.style.display = 'none';
        gen9.style.display = 'block';
    } else {
        alldiv.style.display = 'block'
    }
}



