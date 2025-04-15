function validity_checker(x1, y1, x2, y2) {
    function main_formula(x1, y1, x2, y2) {
        result = Math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

        if (Number.isInteger(result)) {
            console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`)
        } else {
            console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`)
        }
    }

    main_formula(x1, y1, 0, 0)
    main_formula(x2, y2, 0, 0)
    main_formula(x1, y1, x2, y2)
}