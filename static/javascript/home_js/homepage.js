document.querySelector("#create").addEventListener("click", function () {
  document.querySelector(".popup_post").classList.add("active1");
});

document.querySelector(".close_btn1").addEventListener("click", function () {
  document.querySelector(".popup_post").classList.remove("active1");
});

document.querySelector(".comment").addEventListener("click", function () {
  document.querySelector(".popup_comment").classList.add("active2");
});

document.querySelector(".close_btn2").addEventListener("click", function () {
  document.querySelector(".popup_comment").classList.remove("active2");
});

// function likePost(postId) {
//   heartImage = document.getElementById(`heart_img_${postId}`); // find the heart with that particular id

//   if (heartImage.src.endsWith("notification.svg")) {
//     heartImage.src = "{% static 'images/home_images/heart-solid.svg' %}"; // Change to filled heart image
//   } else {
//     heartImage.src = "{% static 'images/home_images/notification.svg' %}"; // Change to notification image
//   }
// }

// Get the scroll position from the session storage
var scrollPosition = sessionStorage.getItem('scrollPosition');

// Scroll to the saved position or the top if no position is saved
window.scrollTo(0, scrollPosition || 0);

// Save the current scroll position in the session storage when the page is unloaded
window.addEventListener('beforeunload', function() {
    sessionStorage.setItem('scrollPosition', window.scrollY);
});