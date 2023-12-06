document.querySelector("#posts_btn").addEventListener('click', function () {
    document.querySelector(".posted_img").style.display = "flex";
    document.querySelector(".saved_img").style.display = "none";
});

document.querySelector("#saved_btn").addEventListener('click', function () {
    document.querySelector(".posted_img").style.display = "none";
    document.querySelector(".saved_img").style.display = "flex";
});