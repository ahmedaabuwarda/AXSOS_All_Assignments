function handleShowMoreBtn(element) {
  element.remove();
}

let clicked = false;
function changeCaruselImg(element) {
  let currentSrc = element.src;
  if (clicked) {
    element.src = "./images/bluecar.png";
    clicked = false;
  } else {
    clicked = true;
    element.src = "./images/blue-super-car.png";
  }
}

function handleServicesBtn(element) {
  // document.getElementById("");
  let cardLayout = element.closest(".card-layout");
  let appointmentCounter = cardLayout.querySelector(
    ".appointment-counter span",
  );
  if (appointmentCounter.textContent > 0) {
    appointmentCounter.innerHTML = Number(appointmentCounter.textContent) - 1;
  }
}

function handleReadMoreReview(element) {
    let reviewContentDiv = element.closest(".reviews-content");
    let reviewContent = reviewContentDiv.querySelector("p");
    console.log(reviewContent);
    reviewContent.innerHTML = "I had a great experience at the car wash. The service was quick and efficent, and my car was cleaned thoroughly with attentionto detail. The staff were professional and committed to providing the best service possible. Additionally, the prices were reasonable considering the quality of the work. I will definitly be comming back and would recommend this car wash to anyone looking for excellent service.";

    let reviewContentImg = reviewContentDiv.querySelector("img");
    reviewContentImg.src = "./images/client.png";
    console.log(reviewContentImg);
}