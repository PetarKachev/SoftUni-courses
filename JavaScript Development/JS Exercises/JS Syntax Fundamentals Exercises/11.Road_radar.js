function road_radar(speed, area) {
    const limitations = {'motorway': 130, 'interstate': 90,
                          'city': 50, 'residential': 20}
    let result = ''

    if (limitations[`${area}`] >= speed) {
        result = `Driving ${speed} km/h in a ${limitations[`${area}`]} zone`
    } else if (limitations[`${area}`] < speed) {

        let speed_difference = speed - limitations[`${area}`]

        if (speed_difference >= 0 && speed_difference <= 20) {
            result = `The speed is ${speed - limitations[`${area}`]} km/h faster than the allowed speed of ${limitations[`${area}`]} - speeding`
        } else if (speed_difference >= 20 && speed_difference <= 40) {
            result = `The speed is ${speed - limitations[`${area}`]} km/h faster than the allowed speed of ${limitations[`${area}`]} - excessive speeding`
        } else if (speed_difference > 40) {
            result = `The speed is ${speed - limitations[`${area}`]} km/h faster than the allowed speed of ${limitations[`${area}`]} - reckless driving`
        }
    }

    console.log(result)
}