function object_creation(first_param, second_param, third_param) {
    let my_object = {};

    my_object.firstName = `${first_param}`;
    my_object.lastName = `${second_param}`;
    my_object.age = `${third_param}`;

    return my_object;
}