function censore_word(text, word) {
    let new_text = text.replaceAll(String(word), '*'.repeat(word.length))

    console.log(new_text)
}