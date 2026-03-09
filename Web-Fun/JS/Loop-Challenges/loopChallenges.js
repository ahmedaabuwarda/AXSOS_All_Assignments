// 1. Display odd numbers from 1 to 20 , Using a loop, create code to print all odd numbers from 1 to 20 in the console.
console.log("Odd numbers from 1 to 20:");
for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}
// 2. Decreasing multiples of 3 , Using a loop, write code to display all numbers that are divisible by 3 from 100 down to 0 in the console.
console.log("Decreasing multiples of 3 from 100 to 0:");
for (let i = 100; i >= 0; i--) {
    if (i % 3 === 0) {
        console.log(i);
    }
}
// 3. Print the given sequence , Using a loop, write code to print the values in the sequence 4, 2.5, 1, -0.5, -2, -3.5 in the console.
console.log("Sequence: 4, 2.5, 1, -0.5, -2, -3.5");
for (let i = 4; i >= -3.5; i -= 1.5) {
    console.log(i);
}
// 4. Sigma ,Write code to calculate the sum of all numbers from 1 to 100 and display the result in the console. The sum should be equivalent to 1 + 2 + 3 + ... + 98 + 99 + 100, which totals 5050.
let sum = 0;
for (let i = 0; i <= 100; i++) {
    sum += i;
}
console.log("The sum of all numbers from 1 to 100 is: " + sum);
// 5. Factorial , Create a program that multiplies all numbers from 1 to 12 and stores the result in a variable called "product". Finally, display the result by using console.log, multiplying 1 * 2 * 3 * ... * 10 * 11 * 12. The final result should be 479001600.
let product = 1;
for (let i = 1; i <= 12; i++) {
    product *= i;
}
console.log("The product of all numbers from 1 to 12 is: " + product);