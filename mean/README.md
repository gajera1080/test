# MEAN Stack Exam-Size Practicals & Revision Guide

Following the PDF pattern: `require()`, `express()`, direct routes, `express.json()`, simple arrays, and simple Mongoose operations.

---

# 1. MongoDB — schoolDB and students (`1_mongodb_queries.js`)

**Remember:** `find → insertMany → updateOne → deleteOne → find`.

---

# 2. Employee Schema + CRUD using Mongoose (`2_employee_crud_mongoose.js`)

Uses Mongoose CRUD methods `create`, `find`, `findByIdAndUpdate`, and `findByIdAndDelete`.

```javascript
const express = require('express');
const mongoose = require('mongoose');

const app = express();

app.use(express.json());

mongoose.connect('mongodb://localhost:27017/companyDB')
    .then(() => console.log('MongoDB Connected'));

// Schema
const employeeSchema = new mongoose.Schema({
    name: String,
    department: String,
    salary: Number,
    experience: Number
});

const Employee = mongoose.model('Employee', employeeSchema);

// CREATE
app.post('/employees', async (req, res) => {
    const employee = await Employee.create(req.body);
    res.json(employee);
});

// READ
app.get('/employees', async (req, res) => {
    const employees = await Employee.find();
    res.json(employees);
});

// UPDATE
app.put('/employees/:id', async (req, res) => {
    const employee = await Employee.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true }
    );

    res.json(employee);
});

// DELETE
app.delete('/employees/:id', async (req, res) => {
    await Employee.findByIdAndDelete(req.params.id);
    res.json({ message: 'Employee deleted' });
});

app.listen(3000, () => {
    console.log('Server is listening at http://localhost:3000');
});
```

---

# 3. ExpressJS Web Server (`3_express_welcome.js`)

```javascript
const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to ExpressJS');
});

app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

### Core pattern
```text
require
   ↓
express()
   ↓
app.get()
   ↓
app.listen()
```

---

# 4. ExpressJS Routes (`4_express_routes.js`)

```javascript
const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to Home Page');
});

app.get('/about', (req, res) => {
    res.send('About Us');
});

app.get('/contact', (req, res) => {
    res.send('Contact Us');
});

app.listen(3000, () => {
    console.log('Server is listening at http://localhost:3000');
});
```

---

# 5. Middleware — Logging + JSON (`5_express_middleware.js`)

```javascript
const express = require('express');

const app = express();

// Middleware
app.use((req, res, next) => {
    console.log('Method:', req.method);
    console.log('URL:', req.url);
    console.log('Time:', new Date());

    next();
});

// JSON middleware
app.use(express.json());

app.post('/student', (req, res) => {
    console.log(req.body);
    res.send('Data received');
});

app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

**Remember:** `req → res → next`.

---

# 6. Static HTML, CSS and Image (`6_express_static.js`)

```javascript
const express = require('express');

const app = express();

app.use(express.static('public'));

app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

---

# 7. REST API — Student Records using Array (`7_student_rest_api_array.js`)

### Memorize the CRUD skeleton
```text
GET     → find / return
POST    → create / push
PUT     → find / change
DELETE  → findIndex / splice
```

---

# 8. REST API — Books (`8_books_rest_api.js`)

Same array REST CRUD pattern as Student Records.

---

# 9. REST API + MongoDB (`9_mongodb_rest_api.js`)

Mongoose + Express REST CRUD pattern.

---

# ⭐ What to Memorize (4 Core Patterns)

### Pattern 1 — Basic Express (Used by Q3, Q4)
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('...');
});

app.listen(3000, () => {
    console.log('Server running');
});
```

### Pattern 2 — Middleware (Used by Q5)
```javascript
app.use((req, res, next) => {
    console.log(req.method);
    console.log(req.url);
    console.log(new Date());
    next();
});

app.use(express.json());
```

### Pattern 3 — Array REST API (Used by Q7, Q8)
```text
GET     → find()
POST    → push()
PUT     → find()
DELETE  → findIndex() + splice()
```

### Pattern 4 — MongoDB/Mongoose (Used by Q2, Q9)
```text
mongoose.connect()
        ↓
Schema
        ↓
Model
        ↓
create()
find()
findByIdAndUpdate()
findByIdAndDelete()
```

| Journal | What you really learn  |
| ------- | ---------------------- |
| **1**   | MongoDB commands       |
| **2**   | Mongoose CRUD          |
| **3**   | Basic Express          |
| **4**   | Express routing        |
| **5**   | Middleware             |
| **6**   | Static files           |
| **7**   | Array REST CRUD        |
| **8**   | Same REST CRUD pattern |
| **9**   | Mongoose + REST        |
