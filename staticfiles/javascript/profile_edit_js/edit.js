function previewImage(input) {
    var preview = document.getElementById('profile-image-preview');
    var file = input.files[0];
    var reader = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    };

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "{% static 'images/home_images/profile.svg' %}";
    }
}
