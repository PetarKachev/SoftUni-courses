function convert_to_object(string) {
    let my_object = JSON.parse(string);
    let keys = Object.keys(my_object);

    for (let key of keys) {
        console.log(`${key}: ${my_object[key]}`)
    }
}