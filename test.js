const express = require('express');
const mysql = require('mysql2');

const app = express();
const port = 3000;

const con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'JHKest24',
    database: 'energy_guardian'
});

app.get('/login', (req, res) => {
    con.connect((err) => {
        if (err) {
            console.error('Can not connect to the database:', err);
            res.status(500).send('Internal Server Error');
            return;
        }

        con.query('SELECT * FROM login', (err, result) => {
            if (err) {
                console.error('Can not execute the query:', err);
                res.status(500).send('Internal Server Error');
                return;
            }

            res.json(result);
            con.end();
        });
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});