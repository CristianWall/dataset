document.addEventListener("DOMContentLoaded", function () {
    // Cargar el archivo CSV
    fetch('./UBIGEO.csv')
        .then(response => {
            // Verificar si el archivo se carga correctamente
            if (!response.ok) {
                throw new Error("No se pudo cargar el archivo CSV");
            }
            return response.text();
        })
        .then(data => {
            // Llamar a la función para procesar los datos CSV
            parseCSV(data);
        })
        .catch(error => {
            console.error("Error al cargar el archivo CSV:", error);
            alert("Hubo un error al cargar el archivo CSV. Revisa la consola para más detalles.");
        });

    // Función para procesar los datos CSV
    function parseCSV(data) {
        // Dividir el archivo CSV en filas
        const rows = data.split('\n');
        const departamentoSelect = document.getElementById('departamento');
        const departamentos = new Set();  // Usamos un Set para evitar duplicados

        // Iterar sobre las filas del CSV
        rows.forEach(row => {
            // Dividir cada fila en columnas
            const columns = row.split(',');
            if (columns.length > 1) {
                const departamento = columns[1].trim(); // Extraemos el nombre del departamento
                if (departamento) {  // Asegurarse de que no se agregue vacío
                    departamentos.add(departamento); // Añadimos al Set
                }
            }
        });

        // Verificar si el Set contiene datos
        console.log("Departamentos encontrados:", departamentos);

        // Llenar el select con los departamentos
        departamentos.forEach(departamento => {
            const option = document.createElement('option');
            option.value = departamento;
            option.textContent = departamento;
            departamentoSelect.appendChild(option);
        });

        // Si no se encuentran departamentos
        if (departamentos.size === 0) {
            alert("No se encontraron departamentos en el archivo CSV.");
        }
    }
});
