function extractText() {
    let list_with_items = document.querySelectorAll('ul#items li');
    let textarea = document.querySelector('#result');

    for (let node of list_with_items) {
        textarea.textContent += node.textContent + '\n';
    }
}