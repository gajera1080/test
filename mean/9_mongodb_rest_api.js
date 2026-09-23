const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());

mongoose.connect("mongodb://127.0.0.1:27017/shopDB");

const Item = mongoose.model("Item", { name: String, price: Number });

// RESTful CRUD API Endpoints
app.get("/items", async (req, res) => res.json(await Item.find()));
app.get("/items/:id", async (req, res) => res.json(await Item.findById(req.params.id)));
app.post("/items", async (req, res) => res.json(await Item.create(req.body)));
app.put("/items/:id", async (req, res) => res.json(await Item.findByIdAndUpdate(req.params.id, req.body, { new: true })));
app.delete("/items/:id", async (req, res) => res.json(await Item.findByIdAndDelete(req.params.id)));

app.listen(3000, () => console.log("Server running on port 3000"));
