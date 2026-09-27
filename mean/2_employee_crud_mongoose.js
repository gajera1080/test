const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/companyDB');

const employeeSchema = new mongoose.Schema({
    name: String,
    department: String,
    salary: Number,
    experience: Number
});

const Employee = mongoose.model('Employee', employeeSchema);

async function crud() {
    // CREATE
    await Employee.create({
        name: 'John',
        department: 'IT',
        salary: 50000,
        experience: 2
    });

    // READ
    let employees = await Employee.find();
    console.log(employees);

    // UPDATE
    await Employee.updateOne(
        { name: 'John' },
        { salary: 60000 }
    );

    // DELETE
    await Employee.deleteOne({ name: 'John' });

    console.log('CRUD completed');
}

crud();
