const express = require('express');
const mongoose = require('mongoose');

const app = express();

app.use(express.json());

mongoose.connect('mongodb://localhost:27017/companyDB')
    .then(() => console.log('MongoDB Connected'));

// Schema
const employeeSchema = new mongoose.Schema({
    name: String,
    department: String,
    salary: Number,
    experience: Number
});

const Employee = mongoose.model('Employee', employeeSchema);

// CREATE
app.post('/employees', async (req, res) => {
    const employee = await Employee.create(req.body);
    res.json(employee);
});

// READ
app.get('/employees', async (req, res) => {
    const employees = await Employee.find();
    res.json(employees);
});

// UPDATE
app.put('/employees/:id', async (req, res) => {
    const employee = await Employee.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true }
    );

    res.json(employee);
});

// DELETE
app.delete('/employees/:id', async (req, res) => {
    await Employee.findByIdAndDelete(req.params.id);
    res.json({ message: 'Employee deleted' });
});

app.listen(3000, () => {
    console.log('Server is listening at http://localhost:3000');
});
