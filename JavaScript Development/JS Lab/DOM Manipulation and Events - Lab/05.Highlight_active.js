function focused() {
    let inputs = document.querySelectorAll('div');

    for (let div of inputs) {
        div.children[1].addEventListener('focus', onFocus)
        div.children[1].addEventListener('blur', onBlur)
    }

    function onFocus(event) {
        console.log(event.target.parentElement.classList.add('focused'))
    }

    function onBlur(event) {
        event.target.parentElement.classList.remove('focused')
    }
}