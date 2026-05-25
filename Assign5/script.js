let selected = "";

function selectCourse(courseName){

    selected = courseName;

    document.getElementById("selectedCourse").innerHTML =
        "✅ " + courseName;

    // Remove previous highlights
    let cards = document.querySelectorAll(".course-card");

    cards.forEach(card=>{
        card.style.border = "none";

        if(card.innerText.includes(courseName)){
            card.style.border = "3px solid #00ffae";
        }
    });
}

/* SUBMIT BUTTON */

function submitCourse(){

    if(selected === ""){
        alert("Please select a course first!");
        return;
    }

    let popup = document.getElementById("popup");

    popup.style.right = "20px";

    setTimeout(()=>{
        popup.style.right = "-300px";
    },3000);
}

/* SEARCH FUNCTION */

document.getElementById("searchBar").addEventListener("keyup", function(){

    let value = this.value.toLowerCase();

    let cards = document.querySelectorAll(".course-card");

    cards.forEach(card=>{

        let text = card.innerText.toLowerCase();

        if(text.includes(value)){
            card.style.display = "block";
        }
        else{
            card.style.display = "none";
        }
    });
});