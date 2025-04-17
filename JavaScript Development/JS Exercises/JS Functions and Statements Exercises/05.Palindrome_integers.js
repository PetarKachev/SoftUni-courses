function palindrom_calculation(array) {
    for (let element of array) {
        let current_element = String(element)
        let reversed_element = []

        for (let i = 0; i < current_element.length; i++) {
            reversed_element.push(current_element[i])
        }

        if (current_element == reversed_element.reverse().join('')) {
            console.log('true')
        } else {
            console.log('false')
        }
    }
}