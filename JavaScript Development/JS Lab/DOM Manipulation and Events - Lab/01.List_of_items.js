function addItem() {
    let input_info = String(document.querySelector('input#newItemText').value);
    let new_li = document.createElement('li')
    new_li.textContent = `${input_info}`
    let ul = document.querySelectorAll('ul#items')[0].appendChild(new_li)
}