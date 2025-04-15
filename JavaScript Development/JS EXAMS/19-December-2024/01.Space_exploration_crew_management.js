function solve(input_info) {
    let number_of_austronauts = Number(input_info[0]);
    let austronauts = {};

    for (let i = 1; i <= number_of_austronauts; i++) {
        let name = input_info[i].split(' ')[0];
        let spacecraft_section = input_info[i].split(' ')[1];
        let skills = input_info[i].split(' ')[2].split(',');

        austronauts[`${name}`] = [spacecraft_section, skills];
    }

    input_info = input_info.slice(number_of_austronauts + 1, input_info.length)

    for (let command of input_info) {
        if (command == 'End') {
            break;
        }

        let action = command.split(' / ')[0];

        if (action == 'Perform') {
            let name = command.split(' / ')[1];
            let spacecraft_section = command.split(' / ')[2];
            let skill = command.split(' / ')[3];

            if (austronauts[name][0] == spacecraft_section && austronauts[name][1].includes(skill)) {
                console.log(`${name} has successfully performed the skill: ${skill}!`)
            } else {
                console.log(`${name} cannot perform the skill: ${skill}.`)
            }

        } else if (action == 'Transfer') {
            let name = command.split(' / ')[1];
            let new_spacecraft_section = command.split(' / ')[2];

            if (austronauts[name]) {
                austronauts[name][0] = new_spacecraft_section;
                console.log(`${name} has been transferred to: ${new_spacecraft_section}`)
            }

        } else if (action == 'Learn Skill') {
            let name = command.split(' / ')[1];
            let new_skill = command.split(' / ')[2];

            if (austronauts[name] && austronauts[name][1].includes(new_skill)) {
                console.log(`${name} already knows the skill: ${new_skill}.`)
            } else if (austronauts[name]) {
                austronauts[name][1].push(new_skill);
                console.log(`${name} has learned a new skill: ${new_skill}.`)
            }
        }
    }

    for (let key of Object.keys(austronauts)) {
        let skills = austronauts[key][1].sort().join(', ');
        console.log(`Astronaut: ${key}, Section: ${austronauts[key][0]}, Skills: ${skills}`)
    }
}