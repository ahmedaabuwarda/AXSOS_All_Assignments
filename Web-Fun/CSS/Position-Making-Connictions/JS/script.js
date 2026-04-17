console.log("page loaded...");

// edit user name
let newName = document.querySelector(".edit-profile-link");
newName.addEventListener("click", (event) => {
  event.preventDefault();
  handleChangeName(event.target);
});

function handleChangeName(element) {
  let newNamePrompt = prompt("Enter new name:");
  document.querySelector(".card-body h1").innerHTML = newNamePrompt;
}

let accept = document.querySelectorAll(".accept-icon");

let close = document.querySelectorAll(".close-icon");

accept.forEach((element) => {
  element.addEventListener("click", (target) => handleAccept(target));
});

close.forEach((element) => {
  element.addEventListener("click", (target) => handleClose(target));
});

function handleAccept(element) {
  let badges = document.querySelectorAll(".badge");
  badges[1].innerHTML = Number(badges[1].innerHTML) + 1;
  badges[0].innerHTML = Number(badges[0].innerHTML) - 1;
  element.target.closest(".card-list-item").remove();
}

function handleClose(element) {
  let badges = document.querySelectorAll(".badge");
  badges[0].innerHTML = Number(badges[0].innerHTML) - 1;
  element.target.closest(".card-list-item").remove();
}
