function odd_and_even_sum(num) {
    let string_num = String(num)
    let even_sum = 0
    let odd_sum = 0

    for (let number of string_num) {
        if (Number(number) % 2 == 0) {
            even_sum += Number(number)
        } else {
            odd_sum += Number(number)
        }
    }

    console.log(`Odd sum = ${odd_sum}, Even sum = ${even_sum}`)
}