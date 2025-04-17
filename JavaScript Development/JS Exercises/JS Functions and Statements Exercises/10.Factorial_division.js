function factorial_calculation(first_num, second_num) {
    let first_num_factorial = 1;
    let second_num_factorial = 1;

    for (let i = 1; i <= first_num; i++) {
        first_num_factorial *= i
    }

    for (let m = 1; m <= second_num; m++) {
        second_num_factorial *= m
    }

    console.log((first_num_factorial / second_num_factorial).toFixed(2))
}