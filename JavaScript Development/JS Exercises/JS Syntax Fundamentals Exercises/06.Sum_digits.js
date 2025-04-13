function sum_digits(nums) {
    let result = 0
    let nums_string = String(nums)

    for (let i = 0; i < nums_string.length; i++) {
        result += Number(nums_string[i])
    }

    console.log(result)
}