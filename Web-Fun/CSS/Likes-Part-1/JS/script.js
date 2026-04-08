function counter(element) {
    // get previous element
    let count = element.previousElementSibling.innerText;
    // split the text
    count = count.split(" ");
    // convert to number and add 1
    count = parseInt(count[0]) + 1;
    // set the new count
    element.previousElementSibling.innerText = count + " like(s)";
}