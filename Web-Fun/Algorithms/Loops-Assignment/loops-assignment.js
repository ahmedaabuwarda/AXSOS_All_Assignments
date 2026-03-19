// Print NumbersWrite a for loop to print numbers from 1 to 10.
for (let i = 1; i <= 10; i++) {
    console.log(i);
}
// Reverse CountingWrite a for loop to print numbers from 10 to 1.
for (let i = 10; i >= 1; i--) {
    console.log(i);
}
// Even NumbersWrite a for loop to print all even numbers between 1 and 20.
for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0) {
        console.log(i);
    }
}
// Odd NumbersWrite a for loop to print all odd numbers between 1 and 20.
for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}
// Sum of NumbersWrite a for loop to calculate and print the sum of numbers from 1 to 10.
let sum = 0;
for (let i = 1; i <= 10; i++) {
    sum += i;
}
console.log(sum);
// FizzBuzzWrite a for loop to print numbers from 1 to 30.
// If the number is divisible by 3, print "Fizz".
// If divisible by 5, print "Buzz".
// If divisible by both 3 and 5, print "FizzBuzz".
for (let i = 1; i <= 30; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}