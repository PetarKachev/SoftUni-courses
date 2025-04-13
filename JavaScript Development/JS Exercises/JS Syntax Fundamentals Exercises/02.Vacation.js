function vacation_calculator(number_people, type_group, day) {
    const prices = { 'Students/Friday': 8.45, 'Students/Saturday': 9.80, 'Students/Sunday': 10.46,
                    'Business/Friday': 10.90, 'Business/Saturday': 15.60, 'Business/Sunday': 16,
                    'Regular/Friday': 15, 'Regular/Saturday': 20, 'Regular/Sunday': 22.50 }

    let current_price = number_people * prices[`${type_group}/${day}`]

    if (type_group == 'Students' && number_people >= 30) {
        current_price -= (current_price * 0.15)
    }

    if (type_group == 'Business' && number_people >= 100) {
        current_price -= (10 * prices[`${type_group}/${day}`])
    }

    if (type_group == 'Regular' && number_people >= 10 && number_people <= 20) {
        current_price -= (current_price * 0.05)
    }

    console.log(`Total price: ${current_price.toFixed(2)}`)
}