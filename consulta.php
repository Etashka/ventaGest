<?php

$serverName = "DESKTOP-RFIB3T7";
$conectionOptions = array("database" => "tu_ddbb", "UID" => "", "PWD" => "");

// Creando conexión:
$conn = sqlsrv_connect($serverName, $conectionOptions);

if ($conn === false) {
    die("Error al conectar con la base de datos: " . print_r(sqlsrv_errors(), true));
}

// Consulta para obtener todos los datos de la base de datos:
$sql = "SELECT * FROM tu_tabla";
$stmt = sqlsrv_query($conn, $sql);

if ($stmt === false) {
    die("Error al ejecutar la consulta SELECT: " . print_r(sqlsrv_errors(), true));
}

// Obtener los datos de la consulta:
$data = array();
while ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
    unset($row['id']);
    $data[] = $row;
}


sqlsrv_close($conn);


header('Content-Type: application/json');
echo json_encode($data);
exit();

?>