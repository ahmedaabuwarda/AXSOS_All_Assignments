// 1. Accessing Elements
let colors = ["red", "blue", "green", "yellow", "purple"];
// print first element
console.log(colors[0]);
// print last element
console.log(colors[colors.length - 1]);
// print element at second position
console.log(colors[1]);
// update the third element to "orange" and print the updated array
colors[2] = "orange";
console.log(colors);

// 2. Traversing an Array
let numbers = [10, 20, 30, 40, 50];
// a. print all elements using a for loop
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
// b. print all the elements in reverse order using a for loop
for(let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}

// 3. searching in an array
// a. check if the number 30 is present in the array and print found at position if found, otherwise print not found
let target = 25;
let numbers2 = [5, 10, 15, 20, 25];
for (let i = 0; i < numbers2.length; i++) {
    if (numbers2[i] === target) {
        console.log(`Found at position ${i}`);
        break;
    }
    if (i === numbers2.length - 1) {
        console.log("Not found");
    }
}

// 4. sorting an array
// a. write a program to sort array in acending order and decending order
let unsortedArray = [50, 20, 70, 10, 40];
// ascending order
unsortedArray.sort((a, b) => a - b);
console.log("Ascending order:", unsortedArray);
// descending order
unsortedArray.sort((a, b) => b - a);
console.log("Descending order:", unsortedArray);
// b. sort array in alpabetical order
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
names.sort();
console.log("Alphabetical order:", names);

// 5. inserting elements
let animals = ["dog", "cat", "rabbit"];
// add elephant to the end of the array
animals.push("elephant");
console.log(animals);
// add lion to the beginning of the array
animals.unshift("lion");
console.log(animals);
// insert tiger between dog and cat
animals.splice(2, 0, "tiger");
console.log(animals);

// 6. deleting elements
let fruits = ["apple", "banana", "cherry", "date"];
// remove the first element
fruits.shift();
console.log(fruits);
// remove the last element
fruits.pop();
console.log(fruits);
// remove banana from the array without using its index
let index = fruits.indexOf("banana");
if (index !== -1) {
    fruits.splice(index, 1);
}
console.log(fruits);

// 7. comping arrays
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
// a. combine two arrays into one array
let combinedArray = array1.concat(array2);
console.log(combinedArray);
// array1.push(...array2); // this called destructive method because it modifies the original array1
// console.log(array1);

// 8. splitting an array
let items = ["a", "b", "c", "d", "e"];
// split the first three elements into a new array and print both arrays
let firstArray = items.slice(0, 3);
let secondArray = items.slice(3);
console.log("First array:", firstArray);
console.log("Second array:", secondArray);

// 9. filtering elements
let numbers3 = [1, 5, 10, 15, 20, 25, 30];
// create a new array containing only the numbers greater than 15 and print the new array
let filteredArray = numbers3.filter(num => num > 15);
console.log(filteredArray);

// 10. advanced challenged
// a. write a program to remove duplicates from an array and print the unique elements
let array = [1, 2, 2, 3, 4, 4, 5];
for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
        if (array[i] === array[j]) {
            array.splice(j, 1);
            j--; // adjust index after removal
        }
    }
}
console.log(array);
// b. write a program to rotate an array to the right by k steps and print the rotated array
let arr = [1, 2, 3, 4, 5];
let n = 2; // number of steps to rotate
for (let i = 0; i < n; i++) {
    arr.unshift(arr.pop());
}
console.log(arr);

// bouns challenge: write a program to merge two sorted arrays into a single sorted array and print the merged array
let sortedArray1 = [1, 3, 5];
let sortedArray2 = [2, 4, 6];
// let sortedArray2 = [6, 7, 8];
// we will define an empty array to hold the merged result and use two pointers to traverse both arrays
let mergedArray = [];
let i = 0, j = 0;
// i will compare the current elements of both arrays and add the smaller one to the merged array, then move the pointer of the array from which the element was taken
// example demonstrating the process of merging two sorted arrays:
//  i
// [1, 3, 5]
//  j
// [2, 4, 6]
while (i < sortedArray1.length && j < sortedArray2.length) {
    if (sortedArray1[i] < sortedArray2[j]) {
        mergedArray.push(sortedArray1[i]);
        i++;
    } else if (sortedArray1[i] > sortedArray2[j]) {
        mergedArray.push(sortedArray2[j]);
        j++;
    }
}
// after comparing all elements, if there are remaining elements in sortedArray1
while (i < sortedArray1.length) {
    mergedArray.push(sortedArray1[i]);
    i++;
}
// if there are remaining elements in sortedArray2
while (j < sortedArray2.length) {
    mergedArray.push(sortedArray2[j]);
    j++;
}
// print the merged array
console.log(mergedArray);