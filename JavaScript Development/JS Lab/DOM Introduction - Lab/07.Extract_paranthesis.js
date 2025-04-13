function extract(content) {
    let string = String(document.querySelector('#content').textContent)
    const regexp = /\(.+?\)/g;
    let result = [];

    let all_matches = [...string.matchAll(regexp)];

    for (let element of all_matches) {
        result.push(element[0].substring(1, element[0].length - 1))
    }

    return result.join('; ')
}