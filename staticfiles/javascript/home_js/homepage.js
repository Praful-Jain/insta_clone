document.querySelector("#create").addEventListener("click", function () {
  document.querySelector(".popup_post").classList.add("active1");
});

document.querySelector(".close_btn1").addEventListener("click", function () {
  document.querySelector(".popup_post").classList.remove("active1");
});

// document.querySelector("#search").addEventListener("click", function () {
//   var searchElement = document.querySelector(".search");
//   var divElement = document.querySelector(".tools button > div");

//   searchElement.classList.toggle("active2");

//   // Check if the "active2" class is present
//   var isActive = searchElement.classList.contains("active2");

//   // Toggle display of paragraphs based on the "active2" class
//   document.querySelectorAll(".tools button > div > p").forEach(function(paragraph) {
//       paragraph.classList.toggle("hide-paragraphs", isActive);
//   });

//   // Toggle width of the div based on the "active2" class
//   divElement.style.width = isActive ? "50%" : "100%"; // or any other appropriate width value
// });


document.getElementById("search").addEventListener("click", function(){
  document.querySelector(".search").classList.toggle("active2");
  
  if (window.innerWidth >= 1300) { 

    // Check if the "active2" class is present
    var isActive =  document.querySelector(".search").classList.contains("active2");
    var divElement = document.querySelector(".navbar");
    var logo = document.querySelector(".navbar > .logo") 
    var icon = document.querySelector(".navbar > .icon")

    document.querySelectorAll(".tools button > div > p").forEach(function(paragraph) {
      paragraph.style.display = isActive ? "none" : "block"; // or any other appropriate display value
    });
  
    divElement.style.width = isActive ? "50px" : "10vw"; // or any other appropriate width value
    logo.style.display = isActive ? "none" : "block";
    icon.style.display = isActive ? "inline" : "none";
    icon.style.height = isActive ? "30px" : "1px";

}
});

// function likePost(postId) {
//   heartImage = document.getElementById(`heart_img_${postId}`); // find the heart with that particular id

//   if (heartImage.src.endsWith("notification.svg")) {
//     heartImage.src = "{% static 'images/home_images/heart-solid.svg' %}"; // Change to filled heart image
//   } else {
//     heartImage.src = "{% static 'images/home_images/notification.svg' %}"; // Change to notification image
//   }
// }



// export default {
//   props: ['post'],
//   methods: {
//     timeAgo(postedOn) {
//       const currentTime = new Date();
//       const postTime = new Date(postedOn);
//       const timeDifference = currentTime - postTime;

//       const minutes = Math.floor(timeDifference / 60000);
//       const hours = Math.floor(minutes / 60);
//       const days = Math.floor(hours / 24);

//       if (days > 0) {
//         return `${days} day${days > 1 ? 's' : ''} ago`;
//       } else if (hours > 0) {
//         return `${hours} hour${hours > 1 ? 's' : ''} ago`;
//       } else if (minutes > 0) {
//         return `${minutes} minute${minutes > 1 ? 's' : ''} ago`;
//       } else {
//         return 'Just now';
//       }
//     },
//   },
// };

// Get the scroll position from the session storage
var scrollPosition = sessionStorage.getItem('scrollPosition');

// Scroll to the saved position or the top if no position is saved
window.scrollTo(0, scrollPosition || 0);

// Save the current scroll position in the session storage when the page is unloaded
window.addEventListener('beforeunload', function() {
    sessionStorage.setItem('scrollPosition', window.scrollY);
});