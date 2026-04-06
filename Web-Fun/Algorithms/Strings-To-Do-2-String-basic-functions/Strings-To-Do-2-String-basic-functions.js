// 1. Reverse String

function reverseString(str) {
  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return reversed;
}
console.log(reverseString("creature")); // "erutaerc"

// 2. Remove Even-Length Strings
function removeEvenLengthStrings(arr) {
  return arr.filter((str) => str.length % 2 !== 0);
}
let arr = ["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."];
arr = removeEvenLengthStrings(arr);
console.log(arr); // ["Nope!", "Its", "Chris", "."]

// 3. Integer to Roman Numeral
// Create a function that converts a given positive integer (less than 4000) into its Roman numeral representation.
// Roman numerals use the following symbols:
// I = 1
// V = 5
// X = 10
// L = 50
// C = 100
// D = 500
// M = 1000
// Example: Given 349, the function should return "CCCIL".
// Given 444, the function should return "CDXLIV".
function intToRoman(num) {
  const romanNumerals = []
}
