const express = require("express");
const app = express();
app.use(express.json());

let students = [{ id: 1, name: "Alice", age: 20 }];

// View all
app.get("/students", (req, res) => res.json(students));

// Add
app.post("/students", (req, res) => {
  const student = { id: students.length + 1, ...req.body };
  students.push(student);
  res.json(student);
});

// Update
app.put("/students/:id", (req, res) => {
  let student = students.find(s => s.id == req.params.id);
  Object.assign(student, req.body);
  res.json(student);
});

// Delete
app.delete("/students/:id", (req, res) => {
  students = students.filter(s => s.id != req.params.id);
  res.json({ message: "Student deleted" });
});

app.listen(3000, () => console.log("Server running on port 3000"));
