function changeLogin(element) {
    if (element.innerText === "Login") {
        element.innerText = "Logout";
    } else {
        element.innerText = "Login";
    }
}

function addDefinition(element) {
    // remove the button
    element.remove();
}

function alertLikes(element) {
    const elementText = element.innerText;
    alert(`Ninja was ${elementText}!`);
}