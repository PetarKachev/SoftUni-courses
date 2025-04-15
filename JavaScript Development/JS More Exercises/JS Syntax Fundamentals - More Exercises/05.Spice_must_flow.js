function spice_must_flow(spice) {
    let days = 0;
    let total_amount = 0;

    while (spice >= 100) {
        total_amount += spice;
        total_amount -= 26;
        if (total_amount < 0) {
            total_amount = 0;
        }
        spice -= 10;
        days += 1;
    }

    total_amount -= 26;
    if (total_amount < 0) {
        total_amount = 0;
    }
    console.log(days);
    console.log(total_amount);
}