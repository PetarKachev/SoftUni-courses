function word_count(sentence, word) {
    let count = 0;

    for (let current_word of sentence.split(' ')) {
        if (current_word == word) {
            count += 1
        }
    }

    console.log(count)
}