function password_validator(password) {
    let pass_length_between_6_10 = false
    let only_letters_and_digits = false
    let at_least_2_digits = false

    if (password.length >= 6 && password.length <= 10) {
        pass_length_between_6_10 = true
    } else {
        console.log("Password must be between 6 and 10 characters")
    }

    if (/^[A-Za-z0-9]+$/.test(password)) {
        only_letters_and_digits = true
    } else {
        console.log("Password must consist only of letters and digits")
    }

    if (/[0-9]{2,}/.test(password)) {
        at_least_2_digits = true
    } else {
        console.log("Password must have at least 2 digits")
    }

    if (pass_length_between_6_10 && only_letters_and_digits && at_least_2_digits) {
        console.log("Password is valid")
    }
}