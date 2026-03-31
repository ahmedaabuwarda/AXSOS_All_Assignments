// 1. Remove Blanks
function removeBlanks(str) {
  return str.split(" ").join("");
}
console.log(removeBlanks(" Pl ayTha tF u nkyM usi c ")); // Output: "PlayThatFunkyMusic"
console.log(removeBlanks("I can not BELIEVE it's not BUTTER")); // Output: "IcannotBELIEVEit'snotBUTTER"

// 2. Get Digits
function getDigits(str) {
  let digits = "";
  for (let i = 0; i < str.length; i++) {
    if (!isNaN(str[i]) && str[i] !== " ") {
      digits += str[i];
    }
  }
  return Number(digits);
}

let digitValue = getDigits("abc8c0d1ngd0j0!8");
console.log(typeof digitValue); // number
console.log(digitValue); // 801008

// 3. Acronyms
function acronym(str) {
  let words = str.split(" ");
  let acronym = "";
  for (let i = 0; i < words.length; i++) {
    if (words[i].length > 0) {
      acronym += words[i][0].toUpperCase();
    }
  }
  return acronym;
}
console.log(acronym(" there's no free lunch - gotta pay yer way. ")); // Output: "TNFL-GPYW"
console.log(acronym("Live from New York, it's Saturday Night!")); // Output: "LFNYISN"

// 4. Count Non-Spaces
function countNonSpaces(str) {
  return str.split(" ").join("").length;
}
console.log(countNonSpaces("Honey pie, you are driving me crazy")); // Output: 29
console.log(countNonSpaces("Hello world !")); // Output: 11

// 5. Remove Shorter Strings
function removeShorterStrings(arr, len) {
  return arr.filter(function (str) {
    return str.length >= len;
  });
}
console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)); // Output: ['Good morning', 'sunshine', 'Earth', 'says', 'hello']
console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3)); // Output: ['There', 'bug', 'the', 'system']