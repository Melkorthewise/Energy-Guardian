<?php
$userName = $_POST["email"];
$password = $_POST["password"];

$host = "localhost";
$username = "root";
$password = "JHKest24!";
$database = "energy_guardians";

$conn = mysqli_connect($host, $username, $password, $database);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "Connected successfully";

mysqli_close($conn);
?>