const sidebar = document.querySelector(".Sign_in_box");
const overlay= document.querySelector(".overlay")

function show_side_bar() {
    sidebar.style.left = "0px";
    overlay.style.display="block";

}

function hide_side_bar() {
    sidebar.style.left = "-350px";
    overlay.style.display="none";
}

