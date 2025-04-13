function even_and_odd_sums(arr) {
    let even_sum = 0;
    let odd_sum = 0;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {
            even_sum += Number(arr[i])
        } else {
            odd_sum += Number(arr[i])
        }
    }

    console.log(even_sum - odd_sum)
}