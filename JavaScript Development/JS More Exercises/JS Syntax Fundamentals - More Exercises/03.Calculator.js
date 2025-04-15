function calculation(first_num, operator, second_num) {
    let result;

    if (operator == '+') {
        result = first_num + second_num
    } else if (operator == '-') {
        result = first_num - second_num
    } else if (operator == '/') {
        result = first_num / second_num
    } else if (operator == '*') {
        result = first_num * second_num
    }

    console.log(result.toFixed(2));
}