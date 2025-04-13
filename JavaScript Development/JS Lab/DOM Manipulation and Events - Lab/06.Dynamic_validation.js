function validate() {
    let input_info = document.getElementById('email');

    input_info.addEventListener('change', validating_email)

    function validating_email(event) {
        let current_text = String(event.target.value)

        if (! /[a-z]+@[a-z]+.[a-z]+/.test(current_text)) {
            event.target.classList.add('error')
        } else {
            event.target.classList.remove('error')
        }
    }
}