function handleNav(element) {
    alert('Loading weather report...');
}

function handleDismiss(element) {
    let ele = document.querySelector('.cookie');
    ele.style.display = 'none';
}

// convert from C to F
function convertToF(C) {
    return (C * 9/5) + 32;
}

function convertToC(F) {
    return (F - 32) * 5/9;
}

function handleTemp(element) {
    let cOrF = element.value;
    let highTemps = document.querySelectorAll('.temp-high');
    let lowTemps = document.querySelectorAll('.temp-low');

    highTemps.forEach(element => {
        let currentTemp = element.innerHTML;
        element.innerHTML = cOrF == 'f' ? Math.round(convertToF(currentTemp)) : Math.round(convertToC(currentTemp));
    });

    lowTemps.forEach(element => {
        let currentTemp = element.innerHTML;
        element.innerHTML = cOrF == 'f' ? Math.round(convertToF(currentTemp)) : Math.round(convertToC(currentTemp));
    });
}