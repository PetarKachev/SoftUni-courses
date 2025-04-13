function solve () {
    let bread_add_button = document.getElementsByClassName('add-product')[0];
    let milk_add_button = document.getElementsByClassName('add-product')[1];
    let tomatoes_add_button = document.getElementsByClassName('add-product')[2];
    let checkout_button = document.getElementsByClassName('checkout')[0];
    let textarea_field = document.getElementsByTagName('textarea')[0];
    let money = 0;
    let list_with_products = new Set();

    bread_add_button.addEventListener('click', bread_button_click)
    milk_add_button.addEventListener('click', milk_button_click)
    tomatoes_add_button.addEventListener('click', tomatoes_button_click)
    checkout_button.addEventListener('click', checkout_click)

    function bread_button_click(event) {
        let product_name = event.target.parentElement.parentElement.children[1].children[0].textContent;
        let product_price = event.target.parentElement.parentElement.children[3].textContent;
        money += Number(product_price);
        list_with_products.add(product_name);
        textarea_field.innerHTML += `Added ${product_name} for ${Number(product_price).toFixed(2)} to the cart.\n`;

    }

    function milk_button_click(event) {
        let product_name = event.target.parentElement.parentElement.children[1].children[0].textContent;
        let product_price = event.target.parentElement.parentElement.children[3].textContent;
        money += Number(product_price);
        list_with_products.add(product_name);
        textarea_field.innerHTML += `Added ${product_name} for ${Number(product_price).toFixed(2)} to the cart.\n`;
    }

    function tomatoes_button_click(event) {
        let product_name = event.target.parentElement.parentElement.children[1].children[0].textContent;
        let product_price = event.target.parentElement.parentElement.children[3].textContent;
        money += Number(product_price);
        list_with_products.add(product_name);
        textarea_field.innerHTML += `Added ${product_name} for ${Number(product_price).toFixed(2)} to the cart.\n`;
    }

    function checkout_click() {
        textarea_field.innerHTML += `You bought ${[...list_with_products].join(', ')} for ${money.toFixed(2)}.`;
        bread_add_button.disabled = true;
        milk_add_button.disabled = true;
        tomatoes_add_button.disabled = true;
        checkout_button.disabled = true;
    }
}