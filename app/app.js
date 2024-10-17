//API REST obtenida a través de Oracle Cloud, referida a la tabla FUSION, formateando los datos que se nos propusieron al empezar el reto según nuestros objetivos de desarrollo
const apiUrl = "https://g35d725d3b5f293-ceroaladerecha.adb.eu-madrid-1.oraclecloudapps.com/ords/usuario/fusion/";

$(document).ready(function() {
    $('#buscar-btn').click(function() {
        const latitud = $('#latitud').val();
        const longitud = $('#longitud').val();
        const radio = $('#radio').val();

        // Validación simple
        if (!latitud || !longitud || !radio) {
            alert("Por favor, completa todos los campos.");
            return;
        }

        // Realiza una solicitud a la API REST
        $.ajax({
            url: apiUrl,
            type: 'GET',
            data: {
                lat: latitud,
                longitud: longitud,
                radius: radio
            },
            success: function(data) {
                // Limpia la lista de embalses
                $('#embalses-list').empty();

                // Log para depurar la respuesta
                console.log("Datos recibidos de la API:", data);

                // Verifica si hay resultados
                if (data && data.items && data.items.length > 0) {
                    // Muestra todos los atributos de cada embalse
                    data.items.forEach(function(embalse) {
                        const embalseDetails = JSON.stringify(embalse, null, 2); // Formatea el objeto en JSON
                        $('#embalses-list').append(`<li class="list-group-item">${embalseDetails}</li>`);
                    });
                } else {
                    $('#embalses-list').append('<li class="list-group-item">No se encontraron embalses cercanos.</li>');
                }
            },
            error: function(xhr, status, error) {
                console.error("Error en la solicitud:", error);
                $('#embalses-list').append('<li class="list-group-item">Error al obtener los datos.</li>');
            }
        });
    });

    // Manejo de la ubicación
    $('#ubicacion-btn').click(function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                $('#latitud').val(position.coords.latitude);
                $('#longitud').val(position.coords.longitude);
            });
        } else {
            alert("Geolocalización no es soportada por este navegador.");
        }
    });
});
