function solve(array) {
    let my_object = {};
    let days_tracker = [];

    for (let element of array) {
        let weekday = element.split(' ')[0];
        let name = element.split(' ')[1];

        if (days_tracker.includes(weekday)) {
            console.log(`Conflict on ${weekday}!`);
        } else {
            my_object[weekday] = name;
            console.log(`Scheduled for ${weekday}`);
            days_tracker.push(weekday);
        }
    }

    for (let key of Object.keys(my_object)) {
        console.log(`${key} -> ${my_object[key]}`);
    }
}