function calculate(first_num, second_num, operator) {
    switch (operator) {
        case "multiply": console.log(first_num * second_num); break;
        case "divide": console.log(first_num / second_num); break;
        case "add": console.log(first_num + second_num); break;
        case "subtract": console.log(first_num - second_num); break;
    }
}