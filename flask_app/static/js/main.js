const returnTopLeft = document.getElementById("back-to-top-left");
const returnTopRight = document.getElementById("back-to-top-right");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop >= 900 || document.documentElement.scrollTop > 900) {
        returnTopLeft.style.display = "block";
        returnTopRight.style.display = "block";
    }   else {
        returnTopLeft.style.display = "none";
        returnTopRight.style.display = "none";
    }
}
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}