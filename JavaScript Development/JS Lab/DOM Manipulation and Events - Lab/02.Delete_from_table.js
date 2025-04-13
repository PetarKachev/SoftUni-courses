function deleteByEmail() {
    let all_tr_elements = document.querySelectorAll('tbody tr');
    let input_info = String(document.querySelector('label input').value);
    let result = document.querySelector('div#result');

    for (let i = 0; i < all_tr_elements.length; i++) {
        let current_mail = String(all_tr_elements[i].children[1].textContent)

        console.log(current_mail)

        if (current_mail == input_info) {
            all_tr_elements[i].remove()
            result.textContent = 'Deleted.'
        }
    }

    if (result.textContent != 'Deleted.') {
        result.textContent = "Not found."
    }
}