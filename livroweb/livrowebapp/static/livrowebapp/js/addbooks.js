document.addEventListener('DOMContentLoaded', function() {
    var saveButton = document.getElementById('Upload');
    var bookForm = document.getElementById('addBookForm');

    if (saveButton && bookForm) {
        saveButton.addEventListener('click', function() {
            bookForm.submit();
        });
    }
});

function addGenre() {
    var genreSelect = document.getElementById("genres");
    var genreInput = document.getElementById("genreText");

    var selectedGenre = genreSelect.options[genreSelect.selectedIndex].value;

    if (genreInput.value === "") {
        genreInput.value = selectedGenre;
    } else {
        genreInput.value += ", " + selectedGenre;
    }
}
