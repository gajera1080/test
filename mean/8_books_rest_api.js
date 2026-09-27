const express = require('express');

const app = express();

app.use(express.json());

let books = [
    { id: 1, title: '1984', author: 'George Orwell' },
    { id: 2, title: 'The Hobbit', author: 'J.R.R. Tolkien' }
];

// GET all books
app.get('/books', (req, res) => {
    res.json(books);
});

// GET book by ID
app.get('/books/:id', (req, res) => {
    const book = books.find(
        b => b.id === parseInt(req.params.id)
    );

    if (!book)
        return res.status(404).send('Book not found');

    res.json(book);
});

// POST
app.post('/books', (req, res) => {
    const newBook = {
        id: books.length + 1,
        title: req.body.title,
        author: req.body.author
    };

    books.push(newBook);

    res.status(201).json(newBook);
});

// PUT
app.put('/books/:id', (req, res) => {
    const book = books.find(
        b => b.id === parseInt(req.params.id)
    );

    if (!book)
        return res.status(404).send('Book not found');

    book.title = req.body.title;
    book.author = req.body.author;

    res.json(book);
});

// DELETE
app.delete('/books/:id', (req, res) => {
    const index = books.findIndex(
        b => b.id === parseInt(req.params.id)
    );

    if (index === -1)
        return res.status(404).send('Book not found');

    const deleted = books.splice(index, 1);

    res.json(deleted[0]);
});

app.listen(5000, () => {
    console.log('Server is listening at http://localhost:5000');
});
