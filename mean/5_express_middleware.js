const express = require('express');

const app = express();

// Middleware
app.use((req, res, next) => {
    console.log('Method:', req.method);
    console.log('URL:', req.url);
    console.log('Time:', new Date());

    next();
});

// JSON middleware
app.use(express.json());

app.post('/student', (req, res) => {
    console.log(req.body);
    res.send('Data received');
});

app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
