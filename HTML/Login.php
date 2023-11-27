

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

        <form class="inlog_boxes" action="../phpLogin.php" method="post">
            <!--E-mailbox, Passwordbox and Submitbutton-->
            <label for="femail">E-mail adress:</label><br>
            <input type="email" placeholder="    example@hotmail.com" name="email"><br><br>
            <label for="fpassword">Password</label><br>
            <input type="password" placeholder="              Password" name="password"><br>

            <a href= "Main.php"><button class="button">Continue</button></a><br>
            <button class="button" onclick="login()">Testing</button><br>
            <!--<a href= "veri.php"><button class="button">SIGN UP</button></a><br>-->
            <!--<button>Testing PHP</button>-->
        </form>
    
        <img class ="login_logo" src="..//Pictures//logo.png">
    </div>

    <div class="bar_down">
        <br>
    </div>
</body>
</html>

