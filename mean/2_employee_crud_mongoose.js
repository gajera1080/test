const mongoose = require('mongoose');
const readline = require('readline');

mongoose.connect('mongodb://localhost:27017/companyDB');

const employeeSchema = new mongoose.Schema({
    name: String,
    department: String,
    salary: Number,
    experience: Number
});

const Employee = mongoose.model('Employee', employeeSchema);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function crud() {
    console.log('\n1. Create');
    console.log('2. Read');
    console.log('3. Update');
    console.log('4. Delete');

    rl.question('Enter your choice: ', async (choice) => {

        switch (choice) {

            case '1':
                await Employee.create({
                    name: 'John',
                    department: 'IT',
                    salary: 50000,
                    experience: 2
                });
                console.log('Employee inserted');
                break;

            case '2':
                let data = await Employee.find();
                console.log(data);
                break;

            case '3':
                await Employee.updateOne(
                    { name: 'John' },
                    { $set: { salary: 60000 } }
                );
                console.log('Employee updated');
                break;

            case '4':
                await Employee.deleteOne({ name: 'John' });
                console.log('Employee deleted');
                break;

            default:
                console.log('Invalid choice');
        }

        rl.close();
        mongoose.connection.close();
    });
}

crud();
