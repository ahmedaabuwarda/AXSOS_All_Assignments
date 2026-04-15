// 1. always hungry
function alwaysHungry(array) {
  let arr = [];
  for (let i = 0; i < array.length; i++) {
    if (array[i] == "food") arr.push("yummy");
  }
  return arr.length > 0 ? arr : "I'm hungry";
}
console.log(alwaysHungry([3.14, "food", "pie", true, "food"]));
// this should console log "yummy", "yummy"
console.log(alwaysHungry([4, 1, 5, 7, 2]));
// this should console log "I'm hungry"

// 2. High Pass Filter

function highPass(arr, cuttoff) {
  let filtered = arr.filter((e) => e > cuttoff);
  return filtered;
}
let result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // we expect back [6, 8, 10, 9]

// 3. Better than average
function betterThanAverage(arr) {
  let sum = 0;
  // calculate the average
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  let filtered = arr.filter((e) => e > sum / arr.length);
  let count = 0;
  // count how many values are greated than the average
  count = filtered.length;
  return count;
}
result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4

// 4. Array Reverse
function reverse(arr) {
  // your code here
  let reversed = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    reversed.push(arr[i]);
  }
  return reversed;
}
result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]

// 5. Fibonacci Array
function fibonacciArray(n) {
  // the [0, 1] are the starting values of the array to calculate the rest from
  let fibArr = [0, 1];
  // your code here
  for (let i = 0; i < n - 2; i++) {
    fibArr.push(fibArr[i] + fibArr[i + 1]);
  }
  return fibArr;
}

result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
