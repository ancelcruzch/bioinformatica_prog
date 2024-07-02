const express = require('express');
const path = require('path');

const app = express();

const file1Route = require('./routes/lab_01');
const file2Route = require('./routes/lab_02');

app.use(express.static(path.join(__dirname, 'public')));

app.use('/api', file1Route);
app.use('/api', file2Route);

app.get('/lab_01', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'file1.html'));
});

app.get('/lab_02', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'file2.html'));
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

module.exports = app;
