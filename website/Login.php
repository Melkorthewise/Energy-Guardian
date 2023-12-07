<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="../style.css">
    <script src="../test.js"></script>
</head>

<body>
    <div class="barUpTxtLeft"><h1 class="guardian">Energy-Guardian</h1></div>

    <div class="bar_up">
        <a href="website/home.php" class="barUpTxtRight">Homepage</a>
        <a href="website/veri.php" class="barUpTxtRight">Sign Up</a>
    </div>

    <div class="mid">
        <h1 class="login_txt">Energy-Guardian</h1>

        <form class="inlog_boxes" action="" method="post">
            <!--E-mailbox, Passwordbox and Submitbutton-->
            <label for="femail">E-mail adress:</label><br>
            <input type="email" placeholder="    example@hotmail.com" name="email"><br><br>
            <label for="fpassword">Password</label><br>
            <input type="password" placeholder="              Password" name="user_password"><br>

            <button class="button" type="submit" name="submit">Continue</button><br>
            <button class="button" onclick="login()">Testing</button><br>
            <a href= "veri.php"><button class="button">SIGN UP</button></a><br>
            <button>Testing PHP</button>
        </form>

        <img class ="login_logo" src="..//Pictures//logo.png">
    </div>

    <div class="bar_down">
        <br>
    </div>
</body>
</html>

<script>
    function login(){
        window.location.href = "Main.php";
    }
</script>

<?php
    // Database connection
    include("databaseCode/serverSetup.php");

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if(isset($_POST['submit'])){
        $email = $_POST['Email_Address'];
        $user_password = $_POST['Password'];

        $sql = "INSERT INTO login (Email_Address, password) VALUES ('$email', '$user_password')";

        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }

    $conn->close();
?>