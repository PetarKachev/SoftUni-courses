function smallest_num(first, second, third) {
    let array = [first, second, third].sort((a, b) => a - b)
    console.log(array[0])
}