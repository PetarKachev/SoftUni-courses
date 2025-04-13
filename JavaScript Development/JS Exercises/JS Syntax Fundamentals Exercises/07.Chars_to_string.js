function chars_to_string(first_par, second_par, third_par) {
    let result = ''
    let list = [first_par, second_par, third_par]

    for (let i = 0; i < list.length; i++) {
        result += String(list[i])
    }

    console.log(result)
}