function check_for_same_nums(num) {
    let result = 0
    let num_str = String(num)
    let same_numbers = true

    for (let i = 0; i < num_str.length; i++) {
        if (num_str[i] != num_str[0]) {
            same_numbers = false
        }
        result += Number(num_str[i])
    }

    console.log(same_numbers)
    console.log(result)
}