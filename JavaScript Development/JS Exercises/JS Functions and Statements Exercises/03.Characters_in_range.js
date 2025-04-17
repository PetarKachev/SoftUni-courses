function calculating_ascii(first_par, second_par) {
    ascii_chars = [
        ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ':', ';', '<', '=', '>', '?', '@',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '[', '\\', ']', '^', '_', '`',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '{', '|', '}', '~'
    ]
    let result = []

    let first_symbol_index = ascii_chars.indexOf(first_par)
    let second_symbol_index = ascii_chars.indexOf(second_par)

    if (first_symbol_index < second_symbol_index) {
        for (let i = first_symbol_index + 1; i < second_symbol_index; i++) {
            result.push(ascii_chars[i])
        }
    }

    if (first_symbol_index > second_symbol_index){
        for (let i = second_symbol_index + 1; i < first_symbol_index; i++) {
            result.push(ascii_chars[i])
        }
    }

    console.log(result.join(' '))
}