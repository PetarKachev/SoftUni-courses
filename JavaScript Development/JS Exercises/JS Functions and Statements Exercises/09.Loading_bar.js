function loading_bar(number) {
    let percentage = `${number}%`
    let loading_bar = []
    let filling = number / 10

    for (let i = 0; i < 10; i++) {
        if (filling > 0) {
            loading_bar.push('%')
            filling -= 1
        } else {
            loading_bar.push('.')
        }
    }

    loading_bar = loading_bar.join('')

    if (loading_bar == '%%%%%%%%%%') {
        console.log(`100% Complete!\n[%%%%%%%%%%]`)
    } else {
        console.log(percentage + ` [${loading_bar}]\nStill loading...`)
    }
}