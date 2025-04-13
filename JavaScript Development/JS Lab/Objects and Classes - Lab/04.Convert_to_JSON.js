function solve(name, lastName, hairColor) {
    let my_object = {name: name,
                     lastName: lastName,
                     hairColor: hairColor
    }

    let json_string = JSON.stringify(my_object);

    console.log(json_string)
}