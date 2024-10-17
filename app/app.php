<?php
header("Content-Type: application/json");

// Verifica si los parámetros de latitud, longitud y radio están presentes
if (!isset($_GET['lat']) || !isset($_GET['long']) || !isset($_GET['radius'])) {
    echo json_encode(["error" => "Parámetros faltantes."]);
    exit;
}

$latitud = $_GET['lat'];
$longitud = $_GET['long'];
$radio = $_GET['radius'];

// URL de la API REST
$apiUrl = "https://g35d725d3b5f293-ceroaladerecha.adb.eu-madrid-1.oraclecloudapps.com/ords/usuario/fusion/";

// Configuración de cURL
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $apiUrl . "?lat=$latitud&long=$longitud&radius=$radio");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Ejecuta la solicitud y obtiene la respuesta
$response = curl_exec($ch);

// Verifica si ocurrió un error en la solicitud
if (curl_errno($ch)) {
    echo json_encode(["error" => "Error en la solicitud: " . curl_error($ch)]);
    curl_close($ch);
    exit;
}

// Cierra cURL
curl_close($ch);

// Devuelve la respuesta de la API al frontend
echo $response;
?>