var mysql = require("mysql2");

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password:"JHKest24", //eigen wachtwoord
    database: "energy_guardian"

});

con.connect(function get(err){
    if (err) throw err;

    con.query("SELECT * FROM login", function(err, result){
        if (err) throw err;
        console.log(result);
    });
});
