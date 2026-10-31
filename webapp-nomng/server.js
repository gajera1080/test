const express = require("express");

const app = express();
app.use(express.json());
app.use(express.static(__dirname + "/public"));
app.use(express.static(__dirname + "/../dependency"));

// In-Memory Array Data Store (No MongoDB Required)
const employees = [
  { employeeId: "E101", name: "John Doe", department: "IT", designation: "Software Engineer", email: "john@example.com", salary: 65000 },
  { employeeId: "E102", name: "Jane Smith", department: "HR", designation: "HR Manager", email: "jane@example.com", salary: 55000 }
];

const notFound = res => res.status(404).json({ error: "Employee not found" });

// CRUD routes
app.get("/api/employees", (req, res) => {
  res.json(employees);
});

app.post("/api/employees", (req, res) => {
  const emp = req.body;
  if (!emp.employeeId || !emp.name) {
    return res.status(400).json({ error: "employeeId and name are required" });
  }
  employees.push(emp);
  res.status(201).json(emp);
});

app.put("/api/employees/:employeeId", (req, res) => {
  const index = employees.findIndex(e => e.employeeId === req.params.employeeId);
  if (index === -1) return notFound(res);
  employees[index] = { ...employees[index], ...req.body };
  res.json(employees[index]);
});

app.delete("/api/employees/:employeeId", (req, res) => {
  const index = employees.findIndex(e => e.employeeId === req.params.employeeId);
  if (index === -1) return notFound(res);
  employees.splice(index, 1);
  res.json({ message: "Employee deleted successfully" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Web App (No-Mongo) running at http://localhost:${PORT}`));
