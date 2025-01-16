const returnTop = document.getElementById("back-to-top");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop >= 1000 || document.documentElement.scrollTop > 1000) {
        returnTop.style.display = "block";
    }   else {
        returnTop.style.display = "none";
    }
}
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}