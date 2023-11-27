<?php
$userName = $_POST["email"];
$password = $_POST["password"];

$host = "localhost";
$userNameDatabase = "root";
$passwordDatabase = "JHKest24";
$databaseName = "energyguardian";

$connect = new mysqli(hostname: $host,
                        username: $userNameDatabase, 
                        password: $passwordDatabase,
                        database: $databaseName,
                        port: 3306);


if(mysqli_connect_errno()){
    die("Connection error: ". $mysqli -> connect_error);
}

echo "Connected";
?>