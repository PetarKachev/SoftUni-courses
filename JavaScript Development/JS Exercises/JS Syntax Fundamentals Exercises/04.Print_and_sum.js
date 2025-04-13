function print_and_sum(start, end) {
    let numbers = []
    let result = 0

    for (let i = start; i <= end; i++) {
        numbers.push(`${i}`)
        result += i
    }

    console.log(numbers.join(' '))
    console.log('Sum: ' + `${result}`)
}