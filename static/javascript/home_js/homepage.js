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

