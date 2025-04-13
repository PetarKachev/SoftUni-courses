function largest_number(num1, num2, num3) {
    if (num1 > num2 & num1 > num3) {
        let result = num1
        return console.log(`The largest number is ${num1}.`)
    } else if (num2 > num1 & num2 > num3) {
        let result = num2
        return console.log(`The largest number is ${num2}.`)
    } else if (num3 > num1 & num3 > num2) {
        let result = num3
        return console.log(`The largest number is ${num3}.`)
    }
}