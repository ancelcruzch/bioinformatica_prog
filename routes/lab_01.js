// routes/file1.js
const express = require('express');
const fs = require('fs');
const path = require('path');
const router = express.Router();

router.get('/lab_01', (req, res) => {
    const filePath = path.join(__dirname, '../data/file1.txt');
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Error al leer file1.txt');
        }
        res.send(data);
    });
});

module.exports = router;
