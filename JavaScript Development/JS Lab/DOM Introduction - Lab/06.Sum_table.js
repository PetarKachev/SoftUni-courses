function sumTable() {
    let all_tr_elements = document.querySelectorAll('table tr');
    let sum = 0;
    let output = document.querySelector('td#sum');

    for (let i = 1; i < all_tr_elements.length; i++) {
        sum += Number(all_tr_elements[i].children[1].textContent);
    }

    output.textContent = sum;
}