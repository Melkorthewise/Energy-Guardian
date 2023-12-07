<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Power usage vieuwer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../style.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script type="text/javascript" src="../Javascript/plotCode.js"></script>
    <script type="text/javascript" src="../Javascript/settingsBehavior.js"></script>
</head>
<body>
    <div class="barUpTxtLeft"><h1 class="guardian">Energy-Guardian</h1></div>
    <div class="bar_up">
        <span class="barUpTxtRight" onclick="inlog()">Log out</span>
        <span class="barUpTxtRight" onclick="openSettings()">Settings</span>
    
        <div style="height:20vh">

        <script type="text/javascript">
            function openSettings() {
                document.getElementById("barDown").style.height="50vh";
            }
            
            function closeSettings() {
                document.getElementById("barDown").style.height = "3vh";

                if(document.getElementById("passwordBar").style.width > "0vw"){
                    closePassword()
                }

                else if(document.getElementById("deviceBar").style.width > "0vw"){
                    closeDevice();
                }
            }

            function inlog(){
                window.location.href="website/Login.php";
            }
        </script>

    </div>

<div id="plot"></div>
<input type="range" id="zoomSlider" min="0" max="5" step="0.1" value="5" style="width: 100%;" />
<script>
var currentZoom = 5;
var yValues = [200, 400, 600, 800, 1000, 1200]; //originele y waarde thingie

function updatePlot() {
    var trace1 = {
        x: [0, 1, 2, 3, 4, 5],
        y: yValues,
        mode: 'lines',
        name: 'testing',
        line: {
          dash: 'dashdot',
          width: 4
        }
    };

    var data = [trace1];
    var layout = {
        title: 'Current power usage',
        xaxis: {
          range: [0, currentZoom],
          autorange: false
        },
        yaxis: {
          range: [0, Math.max(...yValues)],
          autorange: false
        },
        legend: {
          y: 0.5,
          traceorder: 'reversed',
          font: {
            size: 16
          }
        }
    };

    Plotly.react('plot', data, layout);
}

function updateYValues() {
    yValues.push(Math.floor(Math.random()*1000)); 
    yValues.shift(); 
    updatePlot(); 
}

document.addEventListener("DOMContentLoaded", function() {
    updatePlot(); 
    setInterval(updateYValues, 3000); //zorgt voor de 3 seconde vertraging
});

document.getElementById('zoomSlider').addEventListener('input', function(e) {
    currentZoom = e.target.value;
    updatePlot();
});



</script>

</body>
</html>
<div id="barDown" class="bar_down">
        <a href="javascript:void(0)" class="close" onclick="closeSettings()">&times;</a>
        <div class="showTxtBarDown">
            <button href="#" class="settings-button" style="text-decoration:none;" onclick="openPassword()">Change password</button><br>
            <a href="#" class="settings-button" style="text-decoration:none;" onclick="openDevice()">Connect device</a><br>
        </div>

        <div id="passwordBar" class="changePassword">
            <div class="passwordBar">
                <br><br>
                <h1>Change Password</h1>
                <label for="fPassword">Password</label><br>
                <input type="Password" placeholder="              Password"  name="newPassword" id="new"><br></br>

                <label for="fRepeat Password">Repeat Password</label><br>
                <input type="password" placeholder="              Password" name="newPasswordRepeat" id="newRepeat"><br></br>
            </div>

            <button class="button" onclick="changePassword()" value="Submit">Continue</button><br><br>
        </div>

        <div id="deviceBar" class="setDevice">
            <h1>Connect Device</h1>
        </div>

        <script>
            function openPassword(){
                if(document.getElementById("deviceBar").style.width > "0vw"){
                    closeDevice();
                }

                document.getElementById("passwordBar").style.width = "20vw";
                document.getElementById("passwordBar").style.height = "50vh";

            }
            
            function closePassword(){
                document.getElementById("passwordBar").style.width = "0vw";
                document.getElementById("passwordBar").style.height = "3vh";
            }

            function changePassword(){
                var password = document.getElementById("new");
                var repeatPassword = document.getElementById("newRepeat");

                if(password.value == repeatPassword.value){
                    alert(`Password has been changed to ${password.value}`);
                }
                
                else{
                    alert("The 2 passwords were not the same")
                }

                password.value="";
                repeatPassword.value="";
            }
            
            function openDevice(){
                if (document.getElementById("passwordBar").style.width > "0vw"){
                    closePassword()
                }

                document.getElementById("deviceBar").style.width = "20vw";
                document.getElementById("deviceBar").style.height = "50vh";
            }

            function closeDevice(){
                document.getElementById("deviceBar").style.width = "0vw";
                document.getElementById("deviceBar").style.height = "3vh";
            }
            function lightMode(){
                document.getElementById("mid").style.backgroundColor = "whitesmoke";
                var elements = document.getElementsByClassName("mainH3");

                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.color = "black";
                }
            }

            function darkMode(){
                document.getElementById("mid").style.backgroundColor = "black";
                var elements = document.getElementsByClassName("mainH3");

                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.color = "whitesmoke";
                }
            }

            function normalMode(){
                document.getElementById("mid").style.backgroundColor = "lightslategray";
                var elements = document.getElementsByClassName("mainH3");

                for (var i = 0; i < elements.length; i++) {
                    elements[i].style.color = "black";
                }

            }
        </script>
    </div> 

</body>
