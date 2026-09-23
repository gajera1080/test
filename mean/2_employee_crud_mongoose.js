const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1:27017/companyDB");

// Schema
const employeeSchema = new mongoose.Schema({
  name: String,
  department: String,
  salary: Number,
  experience: Number
});

const Employee = mongoose.model("Employee", employeeSchema);

async function crud() {
  // CREATE
  const emp = await Employee.create({ name: "Alice", department: "IT", salary: 70000, experience: 3 });
  console.log("Created:", emp);

  // READ
  console.log("All Employees:", await Employee.find());

  // UPDATE
  await Employee.updateOne({ name: "Alice" }, { salary: 75000 });
  console.log("Updated:", await Employee.findOne({ name: "Alice" }));

  // DELETE
  await Employee.deleteOne({ name: "Alice" });
  console.log("Deleted. Remaining:", await Employee.find());

  mongoose.disconnect();
}

crud();
