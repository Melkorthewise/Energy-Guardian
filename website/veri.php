<?php
    // Database connection
    include("website/databaseCode/serverSetup.php");

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if(isset($_POST['submit'])){
        $firstName = $_POST['firstName'];
        $lastName = $_POST['lastName'];
        $email = $_POST['email'];
        $user_password = $_POST['password'];
        

        $sql = "INSERT INTO login (Email_Address, FirstName, SecondName, Password)
        VALUES ('$email', '$firstName', '$lastName', '$user_password')";
        
        echo $sql;

        if (mysqli_query($conn, $sql))  {
            echo "New record created successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }

    $conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="../style.css">
</head>

<body>
    <div class="barUpTxtLeft"><h1 class="guardian">Energy-Guardian</h1></div>

    <div class="bar_up">
        <a href="home.htm" class="barUpTxtRight">Homepage</a>
    </div>

    <div class="mid">
        <h1 class="login_txt">Energy-Guardian</h1>

        <form class="inlog_boxes" method="post" onsubmit="signUp()">
            <!--E-mailbox, Passwordbox and Submitbutton-->
            <label for="First Name">First Name</label><br>
            <input type="text" placeholder="              First Name" name="firstName" id="firstName"><br></br>

            <label for="Second Name">Last Name</label><br>
            <input type="text" placeholder="              Second Name" name="lastName" id="lastName"><br></br>

            <label for="fEmail">E-mail Adress:</label><br>
            <input type="Email" placeholder="    example@hotmail.com" name="email" id="email"><br><br>

            <label for="fPassword">Password</label><br>
            <input type="Password" placeholder="              Password" name="password" id="password"><br></br>

            <label for="fRepeat Password">Repeat Password</label><br>
            <input type="Password" placeholder="              Password" name="passwordRepeat" id="passwordRepeat"><br></br>

            <input class="button" type="submit">SIGN UP!</input></a>

            
        </form>


        <img class ="login_logo" src="..//Pictures//logo.png">
    </div>

    <div class="bar_down">
        <br>
    </div>
</body>
</html>

<script>
    function signUp(){
        var firstName = document.getElementById("firstName");
        var lastName = document.getElementById("lastName");
        var email = document.getElementById("email");
        var password = document.getElementById("password");
        var repeatPassword = document.getElementById("passwordRepeat");

        if(password.value == repeatPassword.value){
            window.location.href = "website/Login.php";
        }

        else{
            alert("Passwords do not match, try again");
            firstName.value = "";
            lastName.value = "";
            email.value = "";
            password.value = "";
            repeatPassword.value = "";
        }
    }
</script>