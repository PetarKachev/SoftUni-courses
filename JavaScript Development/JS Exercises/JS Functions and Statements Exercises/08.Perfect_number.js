function calculating_perfect_number(num) {
    let divisors = []
    let sum = 0

    for (let i = 1; i < num; i++) {
        if (num % i == 0) {
            divisors.push(i)
        }
    }

    for (let digit of divisors) {
        sum += digit
    }

    if (sum == num) {
        console.log("We have a perfect number!")
    } else {
        console.log("It's not so perfect.")
    }
}