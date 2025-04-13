function circle_radius(argument) {
    let number_type = typeof 5
    let argument_type = typeof argument
    if (number_type !== argument_type) {
        console.log(`We can not calculate the circle area, because we receive a ${argument_type}.`)
    } else {
        console.log((3.14159 * (argument ** 2)).toFixed(2))
    }
}