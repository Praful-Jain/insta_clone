document.querySelector("#create").addEventListener("click", function () {
  document.querySelector(".popup").classList.add("active");
});

document.querySelector(".close_btn").addEventListener("click", function () {
  document.querySelector(".popup").classList.remove("active");
});

// function likePost(postId) {
//   heartImage = document.getElementById(`heart_img_${postId}`); // find the heart with that particular id

//   if (heartImage.src.endsWith("notification.svg")) {
//     heartImage.src = "{% static 'images/home_images/heart-solid.svg' %}"; // Change to filled heart image
//   } else {
//     heartImage.src = "{% static 'images/home_images/notification.svg' %}"; // Change to notification image
//   }
// }
