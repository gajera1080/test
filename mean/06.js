// Consolidated Practicals 7 & 8: In-Memory RESTful API (Complete CRUD: Students & Books)
const express = require("express");
const app = express();
app.use(express.json());

// In-Memory Data Store
let items = [
  { id: 1, name: "Alice", course: "IT", title: "Node.js Guide" },
  { id: 2, name: "Bob", course: "CS", title: "MongoDB Basics" }
];

// 1. GET all records
app.get("/api/items", (req, res) => res.json(items));

// 2. GET single record by ID
app.get("/api/items/:id", (req, res) => {
  const item = items.find(i => i.id == req.params.id);
  item ? res.json(item) : res.status(404).send("Record not found");
});

// 3. POST add new record
app.post("/api/items", (req, res) => {
  const newItem = { id: Date.now(), ...req.body };
  items.push(newItem);
  res.status(201).json(newItem);
});

// 4. PUT update record by ID
app.put("/api/items/:id", (req, res) => {
  const item = items.find(i => i.id == req.params.id);
  if (item) {
    Object.assign(item, req.body);
    res.json(item);
  } else {
    res.status(404).send("Record not found");
  }
});

// 5. DELETE record by ID
app.delete("/api/items/:id", (req, res) => {
  items = items.filter(i => i.id != req.params.id);
  res.send("Deleted successfully");
});

app.listen(3000, () => {
  console.log("In-Memory RESTful API running at http://localhost:3000/api/items");
});
