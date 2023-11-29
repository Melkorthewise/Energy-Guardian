<?php

$userName = $_POST["email"];
$userPassword = $_POST["password"];

$host = "localhost";
$user = "root";
$password = "";
$databaseName = "energyguardian";

$conn = mysqli_connect(hostname:$host, 
                        username:$user, 
                        password:$password, 
                        database:$databaseName);

if(mysqli_connect_errno()){
    die("Error " . mysqli_connect_error());
}


$sql = "SELECT UserID FROM login 
WHERE Email_Address = '$userName' AND PW = '$userPassword'";

$result = $conn->query($sql);


if ($result) {
    header("Location: Main.htm");
    exit;
}

die("ERROR");
?>
