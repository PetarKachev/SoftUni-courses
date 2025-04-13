function solve(array) {
    let my_object = {};

    for (let element of array) {
        let name = element.split(':')[0];
        let address = element.split(':')[1];

        my_object[name] = address;
    }

    let sorted_keys = (Object.keys(my_object)).sort();

    for (let key of sorted_keys) {
        console.log(`${key} -> ${my_object[key]}`);
    }
}