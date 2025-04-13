function addItem() {
    input_info = document.querySelector('input#newItemText');
    ul_list = document.querySelector('ul#items');

    new_li = document.createElement('li');
    new_li.textContent = `${input_info.value}`

    new_button = document.createElement('a');
    new_button.href = '#';
    new_button.textContent = '[Delete]'
    new_button.addEventListener('click', deleting)

    new_li.appendChild(new_button)

    ul_list.appendChild(new_li);

    input_info.value = '';

    function deleting(event) {
        event['target'].parentElement.remove();
    }
}