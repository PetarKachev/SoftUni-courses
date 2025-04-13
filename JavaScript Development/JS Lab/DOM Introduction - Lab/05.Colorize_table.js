function colorize() {
    let items = document.querySelectorAll('tbody tr:nth-child(even)')

    for (let current_item of items) {
        current_item.style.backgroundColor = 'teal';
    }
}