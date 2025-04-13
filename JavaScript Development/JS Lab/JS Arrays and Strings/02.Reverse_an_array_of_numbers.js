function reverse_an_array(num, array) {
    let new_array = []

    for (let i = 0; i < num; i++) {
        new_array.push(array[i])
    }

    console.log((new_array.reverse()).join(' '))
}