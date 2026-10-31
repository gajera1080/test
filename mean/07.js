// Practical 9: RESTful API in Express connected to MongoDB (Mongoose)
const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());

mongoose.connect("mongodb://127.0.0.1:27017/productDB");

const Product = mongoose.model("Product", {
  title: String,
  price: Number,
  category: String
});

// GET all products
app.get("/products", async (req, res) => {
  res.json(await Product.find());
});

// POST create product
app.post("/products", async (req, res) => {
  res.status(201).json(await Product.create(req.body));
});

// PUT update product
app.put("/products/:id", async (req, res) => {
  res.json(await Product.findByIdAndUpdate(req.params.id, req.body, { new: true }));
});

// DELETE remove product
app.delete("/products/:id", async (req, res) => {
  await Product.findByIdAndDelete(req.params.id);
  res.send("Product deleted");
});

app.listen(3000, () => {
  console.log("MongoDB RESTful API running at http://localhost:3000/products");
});
