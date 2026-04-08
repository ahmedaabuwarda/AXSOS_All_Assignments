function pizzaOven(crustType, sauceType, cheeses, toppings) {
    let pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

console.log(pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]));
console.log(pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]));
console.log(pizzaOven("hand tossed", "hotsauce", ["feta"], ["olives", "onions"]));
console.log(pizzaOven("hand tossed", "tomato mix", ["mozzarella"], ["meat", "onions"]));

function randomPizza() {
    let pizza = {};
    let crustTypes = ["deep dish", "hand tossed", "thin crust", "stuffed crust"];
    let sauceTypes = ["traditional", "marinara", "hotsauce", "tomato mix"];
    let cheeses = ["mozzarella", "feta", "cheddar", "parmesan"];
    let toppings = ["pepperoni", "sausage", "mushrooms", "olives", "onions", "meat"];

    pizza.crustType = crustTypes[Math.floor(Math.random() * crustTypes.length)];
    pizza.sauceType = sauceTypes[Math.floor(Math.random() * sauceTypes.length)];
    pizza.cheeses = cheeses[Math.floor(Math.random() * cheeses.length)];
    pizza.toppings = toppings[Math.floor(Math.random() * toppings.length)];

    return pizza;
}

console.log(randomPizza());