function solve(array) {
    let my_object = {}

    for (let element of array) {
        let key = element.split(' ')[0];
        let value = element.split(' ')[1];

        my_object[key] = value;
    }

    let keys = Object.keys(my_object);

    for (let key of keys) {
        console.log(`${key} -> ${my_object[key]}`)
    }
}