<?php
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

    //echo "Connected";
?>

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
        <a href="home.php" class="barUpTxtRight">Homepage</a>
        <a href="veri.php" class="barUpTxtRight">Sign Up</a>
    </div>

    <div class="mid">
        <h1 class="login_txt">Energy-Guardian</h1>

        <form class="inlog_boxes" method="post">
            <!--E-mailbox, Passwordbox and Submitbutton-->
            <label for="femail">E-mail adress:</label><br>
            <input type="email" placeholder="    example@hotmail.com" name="email" id="user"><br><br>
            <label for="fpassword">Password</label><br>
            <input type="password" placeholder="              Password" name="password" id="userPassword"><br>

            <button class="button" onclick="toMainPage()">Continue</button><br>
            <!--<button class="button" onclick="login()">Testing</button><br>-->
            <a href= "veri.php"><button class="button">SIGN UP</button></a><br>
            <!--<button>Testing PHP</button>-->
        </form>
    
        <img class ="login_logo" src="..//Pictures//logo.png">
    </div>

    <div class="bar_down">
        <br>
    </div>
</body>
</html>

<script>
    function toMainPage(){
        var user = document.getElementById("user");
        var userPassword = document.getElementById("userPassword");
        
        <?php
            $sql = "SELECT UserID FROM energyguardian";
        ?>
        //window.location.href = 'Main.php';
    }
</script>
