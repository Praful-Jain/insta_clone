document.querySelector("#create").addEventListener('click',function(){
    document.querySelector(".popup").classList.add("active")
});

document.querySelector(".close_btn").addEventListener('click',function(){
    document.querySelector(".popup").classList.remove("active")
});