const express = require("express");
const app = express();
app.use(express.json());

let books = [{ id: 1, title: "Book A" }];

// GET /books - Get all books
app.get("/books", (req, res) => res.json(books));

// GET /books/:id - Get a book by ID
app.get("/books/:id", (req, res) => res.json(books.find(b => b.id == req.params.id)));

// POST /books - Add a new book
app.post("/books", (req, res) => {
  const book = { id: books.length + 1, ...req.body };
  books.push(book);
  res.json(book);
});

// PUT /books/:id - Update a book by ID
app.put("/books/:id", (req, res) => {
  let book = books.find(b => b.id == req.params.id);
  Object.assign(book, req.body);
  res.json(book);
});

// DELETE /books/:id - Delete a book by ID
app.delete("/books/:id", (req, res) => {
  books = books.filter(b => b.id != req.params.id);
  res.json({ message: "Book deleted" });
});

app.listen(3000, () => console.log("Server running on port 3000"));
