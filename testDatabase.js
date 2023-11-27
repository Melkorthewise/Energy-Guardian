var mysql = require('mysql2');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password:"JHKest24", //eigen wachtwoord
    database: "test" //pas gebruiken na het maken van een database

});

//Creating database
//con.connect(function(err){
    //if(err) throw err;
    //console.log("Connected!");

    //con.query("CREATE DATABASE test", function (err, result){
        //if(err) throw err;
        //console.log("Database");
    //})
//});

//Adding tables
//con.connect(function(err){
    //if(err) throw err;
    //var sql= "CREATE TABLE User (UserName VARCHAR(255), PASSWORD VARCHAR(255))";

    //con.query(sql, function(err, result){
        //if (err) throw err;
        //console.log("Table created");
    //});
//});

//Altering tables
//con.connect(function(err){
    //if (err) throw err;

    //var sql = "ALTER TABLE User ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"; //Geeft automatisch een unieke sleutel
    //con.query(sql, function(err, result){
        //if (err) throw err;
        //console.log("Table altered");
    //});
//});

//Inserting in tables
//con.connect(function(err){
    //if (err) throw err;

    //var sql = "INSERT INTO User (Username, PASSWORD) VALUES ('Hendrik', 'Test123')";
    //con.query(sql, function(err, result){
        //if (err) throw err;
        //console.log("1 record inserted" + result);
    //});
//});

//Selecting from table
//con.connect(function(err){
    //if (err) throw err;

    //con.query("SELECT * FROM User", function(err, result){
        //if (err) throw err;
        //console.log(result);
    //});
//});

//Select with filter
//con.connect(function(err){
    //if (err) throw err;

    //con.query("SELECT * FROM User WHERE UserName='Hendrik'", function(err, result){
        //if (err) throw err;
        //console.log(result);
    //});
//});

//Sort result
//con.connect(function(err){
    //if (err) throw err;

    //con.query("SELECT * FROM User ORDER BY UserName", function(err, result){
        //if (err) throw err;
        //console.log(result);
    //});
//});

//Delete record
//con.connect(function(err){
    //if (err) throw err;
    //var sql = "DELETE FROM User WHERE UserName = 'Hendrik'"
    
    //con.query(sql, function(err, result){
        //if (err) throw err;
        //console.log("Deleted: " + result.affectedRows);
    //});
//});

//Delete table
//con.connect(function(err){
    //if (err) throw err;
    //var sql = "DROP TABLE User";

    //con.query(sql, function(err, result){
        //if (err) throw err;
        //console.log("Deleted");
    //});
//});

//Update table
//con.connect(function(err){
    //if (err) throw err;
    //var sql = "UPDATE User SET PASSWORD = 'NEWPASSWORD!@#$'WHERE UserName = 'Hendrik'";

    //con.query(sql, function(err, result){
        //if (err) throw err;
        //console.log(result.affectedRows + " Updated");
    //});
//});

//Limit the result
//con.connect(function(err){
    //if (err) throw err;
    //var sql = "SELECT * FROM User LIMIT 5"; //Geeft maar maximaal aantal returns
    //con.query("SELECT * FROM User ORDER BY UserName", function(err, result){
        //if (err) throw err;
        //console.log(result);
    //});
//});