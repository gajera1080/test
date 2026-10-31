const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());
app.use(express.static(__dirname + "/public"));
app.use(express.static(__dirname + "/../dependency"));

// 1. Connect to MongoDB
mongoose.connect("mongodb://127.0.0.1:27017/employeeDB")
  .then(() => console.log("Connected to MongoDB (employeeDB)"))
  .catch(err => console.error("MongoDB Connection Error:", err.message));

// 2. Employee model (all fields required)
const required = type => ({ type, required: true });

const Employee = mongoose.model("Employee", new mongoose.Schema({
  employeeId: { ...required(String), unique: true },
  name: required(String),
  department: required(String),
  designation: required(String),
  email: required(String),
  salary: required(Number)
}));

// 3. Helper: wrap a route so any error becomes { error } with the given status
const handle = (errorCode, fn) => async (req, res) => {
  try { await fn(req, res); }
  catch (err) { res.status(errorCode).json({ error: err.message }); }
};

// 4. CRUD routes
app.get("/api/employees", handle(500, async (req, res) => {
  res.json(await Employee.find());
}));

app.post("/api/employees", handle(400, async (req, res) => {
  res.status(201).json(await Employee.create(req.body));
}));

app.put("/api/employees/:employeeId", handle(400, async (req, res) => {
  res.json(await Employee.findOneAndUpdate({ employeeId: req.params.employeeId }, req.body, { new: true }));
}));

app.delete("/api/employees/:employeeId", handle(500, async (req, res) => {
  await Employee.deleteOne({ employeeId: req.params.employeeId });
  res.json({ message: "Employee deleted successfully" });
}));

app.listen(3000, () => console.log("Full-Stack App running at http://localhost:3000"));
