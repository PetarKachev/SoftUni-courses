function calculation(first, second, third) {
    function sum(first_par, second_par) {
        return first_par + second_par
    }

    function subtract(sum_result, third_par) {
        return sum_result - third_par
    }

    console.log(subtract(sum(first, second), third))
}