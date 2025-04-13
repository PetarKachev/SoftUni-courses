function cooking_by_numbers(num, first, second, third, forth, fifth) {
    let number = Number(num)
    let all_elements = [first, second, third, forth, fifth]

    for (let element of all_elements) {
        if (element == 'chop') {
            number /= 2
        } else if (element == 'dice') {
            number = Math.sqrt(number)
        } else if (element == 'spice') {
            number += 1
        } else if (element == 'bake') {
            number *= 3
        } else if (element == 'fillet') {
            number -= (number * 0.20)
        }
        console.log(number)
    }
}