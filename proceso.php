<?php

$serverName = "DESKTOP-RFIB3T7";
$conectionOptions = array("database" => "tu_bbdd","UID" => "","PWD" => "",);

//Creando conexión:

$conn = sqlsrv_connect ($serverName, $conectionOptions);

if ($conn === false){
    die("Error al ejecutar la consulta:" . print_r(sqlsrv_errors(), true));    

}
$nombre = "";
$compania = "";
$pin = "";
$exp = "";
$po = "";
$order = "";
$plan = "";
//Procesamiento de base de datos:
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $nombre = $_POST["name"];
    $compania = $_POST["company"];
    $pin = $_POST["no_pin"];
    $exp = $_POST["date"];
    $po = $_POST["no_po"];
    $order = $_POST["no_order"];
    echo "dentro del if";
    echo "$nombre";
    $planMapping = array(
        "Plan 1.5GB" => "1.5gb",
        "Plan 3GB" => "3gb",
        "Plan 5GB" => "5gb",
        "Plan 10GB" => "10gb",
        "Plan 15GB" => "15gb",
        "Plan 25GB" => "25gb"
    );
    $planSelected = $_POST["plan"];
    $plan = array_search($planSelected, $planMapping);
    if ($plan !== false) {
        $plan = $planMapping[$plan];
    } else {
        die("El plan seleccionado no es válido.");
    }
}


//Consulta para insertar los datos en la bbdd:
$sql = "INSERT INTO tu_tabla (name, company, plan, pin, exp, po, order)  VALUES (?, ?, ?, ?, ?, ?, ?)";
$params = array ($nombre, $compania, $plan, $pin, $exp, $po, $order, );
$stmt = sqlsrv_query($conn, $sql, $params);

if ($stmt === false) {
    die("Error al ejecutar la consulta: " . print_r(sqlsrv_errors(), true));
}

// Consulta para obtener los datos:

$sql = "SELECT * FROM tu_tabla WHERE name = ? AND company = ? AND plan = ? AND pin = ? AND exp = ? AND po = ? AND order = ?";
$params = array($nombre, $compania, $plan, $pin, $exp, $po, $order);
$stmt = sqlsrv_query($conn, $sql, $params);

if ($stmt === false) {
    die("Error al ejecutar la consulta SELECT: " . print_r(sqlsrv_errors(), true));
}


$data = array();
while ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
    unset($row['id']);
    $data[] = $row;
}


sqlsrv_close($conn);


//header('Content-Type: application/json');
//echo json_encode($data);
header("Location: index.html");
exit();

?>