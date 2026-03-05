// JS Assignments Practice-1
// Name: Ahmed Abuwarda, Date 03/03/2026

// Write a program that checks if a number is positive or negative.
let number = -5; // You can change this value to test different numbers
if (number > 0) {
  console.log("The number is positive.");
} else if (number < 0) {
  console.log("The number is negative.");
} else {
  console.log("The number is zero.");
}

// Write a program that prints "Good morning" if the time is less than 12 and "Good afternoon" otherwise.
let time = 10; // You can change this value to test different times
if (time < 12) {
  console.log("Good morning");
} else {
  console.log("Good afternoon");
}

/*
Write a program that assigns grades based on scores:
90 and above: A
80–89: B
70–79: C
Below 70: F
*/
let score = 85; // You can change this value to test different scores
if (score >= 90) {
  console.log("A");
} else if (score >= 80) {
  console.log("B");
} else if (score >= 70) {
  console.log("C");
} else {
  console.log("F");
}
// Write a program that takes a day of the week and prints whether it’s a weekday or weekend.
let day = "Saturday"; // You can change this value to test different days
if (day === "Saturday" || day === "Sunday") {
  console.log("It's a weekend!");
} else if (
  day === "Monday" ||
  day === "Tuesday" ||
  day === "Wednesday" ||
  day === "Thursday" ||
  day === "Friday"
) {
  console.log("It's a weekday!");
} else {
  console.log("Wrong day!");
}
