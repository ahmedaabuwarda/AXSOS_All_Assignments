// Create a program that will iterate through each number from 1 to 100 and:
// Output "Fizz" for multiples of 3
// Output "Buzz" for multiples of 5
// Output "FizzBuzz" for numbers that are multiples of both 3 and 5
// For all other numbers, just print the number.
for (let i = 1; i <= 100; i++) {
  // the reason we check for multiples of both 3 and 5 first is because if we check for 3 or 5 first, we would never reach the condition for multiples of both, since those numbers would already be caught by the previous conditions.
  if (i % 3 == 0 && i % 5 == 0) {
    console.log("FizzBuzz");
  } else if (i % 3 == 0) {
    console.log("Fizz");
  } else if (i % 5 == 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}
