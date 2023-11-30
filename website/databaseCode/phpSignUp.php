<?php

$firstName = $_POST["firstName"];
$lastName = $_POST["lastName"];
$email = $_POST["email"];
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

$sqlOutput = "SELECT UserID FROM login ORDER BY UserID DESC";
if ($conn->query($sqlOutput) === TRUE) {
    $last_id = $conn->insert_id +1;

    $sql = "INSERT INTO login (UserID, Email_Adress, FirstName, SecondName, PW)
    VALUES ('$last_id', '$email', '$firsName', '$lastName', '$password')";
    $result = $conn->query($sql);


    if ($result) {
        header("Location: Main.php");
        exit;
    }

    die("ERROR" . mysqli_connect_error());
    }

else{
    die("Error" . mysqli_connect_error());
}

?>
