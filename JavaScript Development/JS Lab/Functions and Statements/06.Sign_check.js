function sign_check(first_num, second_num, third_num) {
    let positive_numbers = 0;
    let negative_numbers = 0;
    let array = [first_num, second_num, third_num];

    for (let i = 0; i < array.length; i++) {
        if (array[i] >= 0) {
            positive_numbers += 1;
        } else {
            negative_numbers += 1;
        }
    }

    if (positive_numbers == 3 | negative_numbers == 2) {
        console.log(`Positive`);
    } else {
        console.log(`Negative`);
    }
}