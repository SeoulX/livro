document.addEventListener('DOMContentLoaded', function() {
    var saveButton = document.getElementById('Upload');
    var bookForm = document.getElementById('addBookForm');

    if (saveButton && bookForm) {
        saveButton.addEventListener('click', function() {
            bookForm.submit();
        });
    }
});