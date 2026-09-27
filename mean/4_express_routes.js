const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to Home Page');
});

app.get('/about', (req, res) => {
    res.send('About Us');
});

app.get('/contact', (req, res) => {
    res.send('Contact Us');
});

app.listen(3000, () => {
    console.log('Server is listening at http://localhost:3000');
});
