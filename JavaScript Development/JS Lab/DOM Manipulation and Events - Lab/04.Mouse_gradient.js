function attachGradientEvents() {
    let gradient = document.getElementById('gradient');
    let output = document.querySelector('div#result');

    gradient.addEventListener('mousemove', onMove);

    function onMove(event) {
        let box = event.target;
        let result = String(Math.floor(event.offsetX / box.clientWidth * 100));
        output.textContent = `${result}%`
    }
}