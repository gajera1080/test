// Practical 2: Employee CRUD using Node.js and Mongoose
const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1:27017/companyDB");

// Employee Schema & Model
const Employee = mongoose.model("Employee", {
  name: String,
  department: String,
  salary: Number,
  experience: Number
});

async function runCRUD() {
  try {
    // 1. Create (Insert)
    const emp = await Employee.create({ name: "Rahul", department: "IT", salary: 50000, experience: 3 });
    console.log("Created Employee:", emp);

    // 2. Read (Find All)
    const allEmps = await Employee.find();
    console.log("All Employees:", allEmps);

    // 3. Update
    await Employee.updateOne({ name: "Rahul" }, { salary: 60000 });
    console.log("Updated Rahul's Salary to 60000");

    // 4. Delete
    await Employee.deleteOne({ name: "Rahul" });
    console.log("Deleted Rahul");
  } catch (err) {
    console.error(err);
  } finally {
    mongoose.connection.close();
  }
}

runCRUD();
