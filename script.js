// script.js

function predict() {
    const marge = document.getElementById('marge').value;
    const liquidite = document.getElementById('liquidite').value;
    const endettement = document.getElementById('endettement').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ marge, liquidite, endettement })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = `Probabilité de faillite : ${data.probabilite}%`;
    })
    .catch(error => console.error('Error:', error));
}
