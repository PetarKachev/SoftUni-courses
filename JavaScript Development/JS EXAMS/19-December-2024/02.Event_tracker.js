function solve() {
    let save_button = document.querySelector('button#save');
    let delete_button = document.getElementsByClassName('btn delete')[0];
    let upcoming_events_list = document.querySelector('ul#upcoming-list');
    let ended_events_list = document.querySelector('ul#events-list');

    delete_button.addEventListener('click', deleting)

    save_button.addEventListener('click', save_information)

    function save_information(event) {
        let name = event.target.parentElement.children[1];
        let note = event.target.parentElement.children[3];
        let date = event.target.parentElement.children[5];

        if (name.value && note.value && date.value) {
            let name_par = document.createElement('p');
            let note_par = document.createElement('p');
            let date_par = document.createElement('p');
            name_par.textContent = `Name: ${name.value}`;
            note_par.textContent = `Note: ${note.value}`;
            date_par.textContent = `Date: ${date.value}`;

            let new_article = document.createElement('article');
            new_article.appendChild(name_par);
            new_article.appendChild(note_par);
            new_article.appendChild(date_par);

            let new_div = document.createElement('div');
            new_div.className = 'event-container';
            new_div.appendChild(new_article);

            let new_li = document.createElement('li');
            new_li.className = 'event-item';
            new_li.appendChild(new_div);

            let new_buttons_div = document.createElement('div');
            new_buttons_div.className = 'buttons';

            let edit_btn = document.createElement('button');
            edit_btn.addEventListener('click', edit_button)
            edit_btn.textContent = 'Edit';
            edit_btn.className = 'btn edit';

            let done_btn = document.createElement('button');
            done_btn.addEventListener('click', done_button)
            done_btn.textContent = 'Done';
            done_btn.className = 'btn done'

            new_buttons_div.appendChild(edit_btn);
            new_buttons_div.appendChild(done_btn);

            new_div.appendChild(new_buttons_div);

            upcoming_events_list.appendChild(new_li);

            name.value = '';
            note.value = '';
            date.value = '';
        } else {
            return;
        }
    }

    function done_button (event) {
        let new_li = document.createElement('li');
        new_li.className = 'event-item';

        let new_article = document.createElement('article');
        new_li.appendChild(new_article);

        let name_par = document.createElement('p');
        let note_par = document.createElement('p');
        let date_par = document.createElement('p');
        name_par.textContent = event.target.parentElement.parentElement.children[0].children[0].textContent;
        note_par.textContent = event.target.parentElement.parentElement.children[0].children[1].textContent;
        date_par.textContent = event.target.parentElement.parentElement.children[0].children[2].textContent;

        new_article.appendChild(name_par);
        new_article.appendChild(note_par);
        new_article.appendChild(date_par);

        ended_events_list.appendChild(new_li);

        event.target.parentElement.parentElement.parentElement.remove()
    }

    function edit_button (event) {
        let name = event.target.parentElement.parentElement.children[0].children[0].textContent.split(': ')[1];
        let note = event.target.parentElement.parentElement.children[0].children[1].textContent.split(': ')[1];
        let date = event.target.parentElement.parentElement.children[0].children[2].textContent.split(': ')[1];
        document.querySelector('input#event').value = name;
        document.querySelector('input#note').value = note;
        document.querySelector('input#date').value = date;

        event.target.parentElement.parentElement.parentElement.remove()
    }

    function deleting() {
        for (let element of [...ended_events_list.children]) {
            element.remove()
        }
    }
}