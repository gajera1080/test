const express = require('express');

const app = express();

app.use(express.json());

let students = [
    { id: 1, name: 'John', age: 18, grade: 'A' },
    { id: 2, name: 'Alice', age: 17, grade: 'B' }
];

// GET
app.get('/students', (req, res) => {
    res.json(students);
});

// GET by ID
app.get('/students/:id', (req, res) => {
    const student = students.find(
        s => s.id === parseInt(req.params.id)
    );

    if (!student)
        return res.status(404).send('Student not found');

    res.json(student);
});

// POST
app.post('/students', (req, res) => {
    const newStudent = {
        id: students.length + 1,
        name: req.body.name,
        age: req.body.age,
        grade: req.body.grade
    };

    students.push(newStudent);

    res.status(201).json(newStudent);
});

// PUT
app.put('/students/:id', (req, res) => {
    const student = students.find(
        s => s.id === parseInt(req.params.id)
    );

    if (!student)
        return res.status(404).send('Student not found');

    student.name = req.body.name;
    student.age = req.body.age;
    student.grade = req.body.grade;

    res.json(student);
});

// DELETE
app.delete('/students/:id', (req, res) => {
    const index = students.findIndex(
        s => s.id === parseInt(req.params.id)
    );

    if (index === -1)
        return res.status(404).send('Student not found');

    const deleted = students.splice(index, 1);

    res.json(deleted[0]);
});

app.listen(5000, () => {
    console.log('Server is listening at http://localhost:5000');
});
