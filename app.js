new Vue({
    el: '#app',
    data: {
        nombre: '',
        telefono: ''
    },
    methods: {
        submitForm() {
            const data = {
                nombre: this.nombre,
                telefono: this.telefono
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
                // Aquí puedes agregar cualquier lógica adicional después de enviar los datos
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }
});

const app = Vue.createApp({
    // ... Resto del código Vue ...
    methods: {
        mostrarReporte() {
            fetch('/reporte')
                .then(response => response.json())
                .then(data => this.mostrarTabla(data))
                .catch(error => console.error(error));
        },
        mostrarTabla(data) {
            const container = document.getElementById('reporte-container');
            const table = document.createElement('table');
            const tbody = document.createElement('tbody');

            // Crea las filas de la tabla con los datos recibidos
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

app.mount('#app');