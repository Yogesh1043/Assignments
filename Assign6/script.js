/* LIVE CLOCK */

setInterval(() => {

    let now = new Date();

    document.getElementById("clock").innerHTML =
        now.toLocaleTimeString();

},1000);


/* SHOW/HIDE ANNOUNCEMENTS */

function toggleAnnouncements(){

    let box =
        document.getElementById("announcementBox");

    if(box.style.display === "none"){
        box.style.display = "block";
    }
    else{
        box.style.display = "none";
    }
}


/* NOTIFICATION POPUP */

function showNotification(){

    let popup =
        document.getElementById("popup");

    popup.style.right = "20px";

    setTimeout(() => {

        popup.style.right = "-400px";

    },3000);
}


/* RESOURCE BUTTON */

function downloadAlert(){

    alert("Resource Download Started!");
}


/* ACTIVE MENU */

let menuItems =
    document.querySelectorAll(".menu li");

menuItems.forEach(item => {

    item.addEventListener("click", () => {

        document
            .querySelector(".active")
            .classList.remove("active");

        item.classList.add("active");
    });

});