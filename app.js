new Vue({
    el: '#app',
    methods: {
        mostrarReporte() {
            fetch('http://localhost:5000/reporte')
                .then(response => response.json())
                .then(data => this.mostrarTabla(data))
                .catch(error => console.error(error));
        },
        mostrarTabla(data) {
            const container = document.getElementById('reporte-container');
            const table = document.createElement('table');
            const tbody = document.createElement('tbody');

            data.forEach(item => {
                const row = document.createElement('tr');
                const nombreCell = document.createElement('td');
                const telefonoCell = document.createElement('td');

                nombreCell.textContent = item.nombre;
                telefonoCell.textContent = item.telefono;

                row.appendChild(nombreCell);
                row.appendChild(telefonoCell);
                tbody.appendChild(row);
            });

            table.appendChild(tbody);
            container.innerHTML = '';
            container.appendChild(table);
        }
    }
});

document.getElementById('formulario').addEventListener('submit', event => {
    event.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const telefono = document.getElementById('telefono').value;

    const data = {
        nombre: nombre,
        telefono: telefono
    };

    fetch('http://localhost:5000/form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('nombre').value = '';
        document.getElementById('telefono').value = '';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
