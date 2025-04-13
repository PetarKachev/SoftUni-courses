function order(product, number) {
    let coffee_price = 1.50;
    let water_price = 1.00;
    let coke_price = 1.40;
    let snacks_price = 2.00;
    let price;

    if (product == 'coffee') {
        price = number * coffee_price;
    } else if (product == 'water') {
        price = number * water_price;
    } else if (product == 'coke') {
        price = number * coke_price;
    } else if (product == 'snacks') {
        price = number * snacks_price;
    }

    console.log(price.toFixed(2));
}