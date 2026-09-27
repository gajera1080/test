const mongoose = require("mongoose");

async function connectDB() {
    await mongoose.connect("mongodb://localhost:27017/companyDB");
    console.log("MongoDB connected");
}

const Employee = mongoose.model("Employee", {
    name: String,
    department: String,
    salary: Number,
    experience: Number
});

async function CRUD() {

    // Create
    await Employee.create({
        name: "John",
        department: "IT",
        salary: 50000,
        experience: 2
    });
    console.log("Employee inserted");

    // Read
    const data = await Employee.find();
    console.log(data);

    // Update
    await Employee.updateOne(
        { name: "John" },
        { salary: 60000 }
    );
    console.log("Employee updated");

    // Delete
    await Employee.deleteOne({ name: "John" });
    console.log("Employee deleted");
}

async function main() {
    await connectDB();
    await CRUD();
}

main();
