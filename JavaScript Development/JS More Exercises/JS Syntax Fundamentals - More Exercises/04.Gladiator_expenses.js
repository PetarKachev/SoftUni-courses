// equipment = (helmet, sword, shield, armor) // We receive Peter's lost fights count

// if count % 2 == 0 => helmet breaks
// if count % 3 == 0 => sword breaks
// if count % 2 == 0 && count % 3 == 0 => shield breaks
// if shield_break % 2 == 0 => armor breaks

function gladiator_expenses(lost_fights_count, helmet_price, sword_price, shield_price, armor_price) {
    let helmet_breaks_num = 0;
    let sword_breaks_num = 0;
    let shield_breaks_num = 0;
    let armor_breaks_num;
    let expenses = 0;

    for (let i = 1; i <= lost_fights_count; i++) {
        if (i % 2 == 0 && i % 3 == 0) {
            shield_breaks_num += 1;
            expenses += shield_price;
            if (shield_breaks_num % 2 == 0) {
                armor_breaks_num += 1;
                expenses += armor_price;
            }
        }

        if (i % 2 == 0) {
            helmet_breaks_num += 1;
            expenses += helmet_price;
        }

        if (i % 3 == 0) {
            sword_breaks_num += 1;
            expenses += sword_price;
        }
    }

    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`)
}