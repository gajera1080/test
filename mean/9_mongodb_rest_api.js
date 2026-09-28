const express = require('express');
const mongoose = require('mongoose');

const app = express();

app.use(express.json());

// Connect MongoDB
mongoose.connect('mongodb://localhost:27017/schoolDB')
    .then(() => console.log('MongoDB Connected'));

// Schema
const studentSchema = new mongoose.Schema({
    name: String,
    age: Number,
    grade: String
});

// Model
const Student = mongoose.model('Student', studentSchema);

// GET
app.get('/students', async (req, res) => {
    const students = await Student.find();
    res.json(students);
});

// GET by Id
app.get('/students/:id', async (req, res) => {
    const students = await User.findById(req.params.id);  
    res.json(students);
});
    
// POST
app.post('/students', async (req, res) => {
    const student = await Student.create(req.body);
    res.json(student);
});

// PUT
app.put('/students/:id', async (req, res) => {
    const student = await Student.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true }
    );

    res.json(student);
});

// DELETE
app.delete('/students/:id', async (req, res) => {
    await Student.findByIdAndDelete(req.params.id);

    res.json({
        message: 'Student deleted'
    });
});

app.listen(3000, () => {
    console.log('Server is listening at http://localhost:3000');
});
