function solve(array) {
    for (let element of array) {
        let word = element.split(' ')[0];
        let num = element.split(' ')[1];

        console.log(`${word}, age ${num} says Meow`)
    }
}