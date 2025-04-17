function matrix_creating(num) {
    for (let i = 0; i < num; i++) {
        let current_row = []

        for (let i = 0; i < num; i++) {
            current_row.push(`${num}`)
        }

        console.log(current_row.join(' '))
    }
}