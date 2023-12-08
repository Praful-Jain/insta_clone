document.querySelector("#posts_btn").addEventListener('click', function () {
    document.querySelector(".posted_img").style.display = "flex";
    document.querySelector(".saved_img").style.display = "none";
});

document.querySelector("#saved_btn").addEventListener('click', function () {
    document.querySelector(".posted_img").style.display = "none";
    document.querySelector(".saved_img").style.display = "flex";
});




document.addEventListener('DOMContentLoaded', function () {
    var deleteButtons = document.querySelectorAll('.delete');
    var deleteModal = document.getElementById('deleteModal');
    var confirmDeleteButton = document.getElementById('confirmDelete');
    var cancelDeleteButton = document.getElementById('cancelDelete');

    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            // Get the post ID from the data attribute
            var postId = button.getAttribute('data-post-id');
            // Set the post ID in the modal for reference
            deleteModal.setAttribute('data-post-id', postId);
            // Show the modal
            deleteModal.style.display = 'block';
        });
    });

    confirmDeleteButton.addEventListener('click', function () {
        // Get the post ID from the modal
        var postId = deleteModal.getAttribute('data-post-id');
        // TODO: Perform the actual delete action using AJAX or a form submission
        // Example: window.location.href = '/delete-post/' + postId;
        // Close the modal
        deleteModal.style.display = 'none';
    });

    cancelDeleteButton.addEventListener('click', function () {
        // Close the modal without performing the delete action
        deleteModal.style.display = 'none';
    });
});