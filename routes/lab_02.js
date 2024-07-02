// routes/file2.js
const express = require('express');
const fs = require('fs');
const path = require('path');
const router = express.Router();

router.get('/lab_02', (req, res) => {
    const filePath = path.join(__dirname, '../data/file2.txt');
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Error reading file2.txt');
        }
        res.send(data);
    });
});

module.exports = router;