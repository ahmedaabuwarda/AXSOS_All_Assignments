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
let arr = [
  "Nope!",
  "Its",
  "Kris",
  "starting",
  "with",
  "K!",
  "(instead",
  "of",
  "Chris",
  "with",
  "C)",
  ".",
];
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
  const romanNumerals = [];
  const symbols = [
    { value: 1000, symbol: "M" },
    { value: 900, symbol: "CM" },
    { value: 500, symbol: "D" },
    { value: 400, symbol: "CD" },
    { value: 100, symbol: "C" },
    { value: 90, symbol: "XC" },
    { value: 50, symbol: "L" },
    { value: 40, symbol: "XL" },
    { value: 20, symbol: "XX" },
    { value: 10, symbol: "X" },
    { value: 9, symbol: "IX" },
    { value: 5, symbol: "V" },
    { value: 4, symbol: "IV" },
    { value: 2, symbol: "II" },
    { value: 1, symbol: "I" },
  ];

  for (let i = 0; i < symbols.length; i++) {
    const { value, symbol } = symbols[i];
    // check cause some numbers are wrong
    while (num >= value) {
      romanNumerals.push(symbol);
      num -= value;
    }
  }

  return romanNumerals.join("");
}
// test
console.log(intToRoman(349)); // "CCCIL"
console.log(intToRoman(444)); // "CDXLIV"
console.log(intToRoman(448)); // "CDXLVIII"

// 4. Roman Numerals to IntegerTask:
// Write a function that converts a Roman numeral string into its corresponding integer value.
// The function should correctly interpret Roman numeral rules, where, for example:
// III = 3DCIX = 609
// MXDII = 1492
// Example Code:
// function romanToInt(roman) {
// // Implementation here
// }
// console.log(romanToInt("III")); // 3
// console.log(romanToInt("DCIX")); // 609
// console.log(romanToInt("MXDII")); // 1492

function romanToInt(s) {
  const map = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let total = 0;

  for (let i = 0; i < s.length; i++) {
    let currentVal = map[s[i]];
    let nextVal = map[s[i + 1]];

    // If current value is less than next value, subtract it
    if (nextVal > currentVal) {
      total -= currentVal;
    } else {
      total += currentVal;
    }
  }

  return total;
}

// Test cases
console.log(romanToInt("III")); // 3
console.log(romanToInt("DCIX")); // 609
console.log(romanToInt("MXDII")); // 1492 (M + D - X + I + I = 1000+500-10+1+1)
