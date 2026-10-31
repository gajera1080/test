# MEAN Stack Practical & Syllabus Solutions (External Exam Suite)

> **Complete University Syllabus & Exam-Ready Code for MEAN Stack**  
> Units 1 to 4: MongoDB, ExpressJS, AngularJS, and NodeJS Fundamentals.  
> Every program in `mean/` is a **single-file code** named simply as `01` to `16`.  
> The master full-stack MEAN application is in `webapp/`.

---

## 📁 Repository Structure

```
test/
├── mean/                                        # All Practicals (Single-File Codes: 01 to 16)
│   ├── 01.js                                   # Practical 1: MongoDB Shell Database, InsertMany, Find, Update, Delete
│   ├── 02.js                                   # Practical 2: Employee Mongoose Schema & CRUD Operations
│   ├── 03.js                                   # Consolidated Practicals 3 & 4: Express Web Server & Routes (/, /about, /contact)
│   ├── 04.js                                   # Practical 5: Express Middleware (Request Logger & JSON Parser)
│   ├── 05.js                                   # Practical 6: Express Static Resource Server (express.static)
│   ├── 06.js                                   # Consolidated Practicals 7 & 8: In-Memory REST API (Full Array CRUD)
│   ├── 07.js                                   # Practical 9: Express RESTful API with MongoDB (Mongoose)
│   ├── 08.js                                   # Syllabus 4.3: Pure NodeJS Web Server (http.createServer)
│   ├── 09.js                                   # Syllabus 4.2.1: NodeJS Core Modules (fs, path, os)
│   ├── 10.js                                   # Syllabus 4.2.2: NodeJS Local Modules (Exporting & Importing)
│   ├── 11.html                                 # Consolidated Q1, Q3, Q6: AngularJS Expressions & Profile
│   ├── 12.html                                 # Consolidated Q2 & Q7: AngularJS Numbers & Multiplication Table
│   ├── 13.html                                 # Consolidated Q4 & Q5: AngularJS Marks, Total, Average & Pass/Fail
│   ├── 14.html                                 # Consolidated Q8 & Q9: AngularJS Custom Directives (<user-card> & <student-card>)
│   ├── 15.html                                 # Practical 10: AngularJS User Registration Form Validation
│   └── 16.html                                 # Practical 11: AngularJS Task Manager (To-Do App)
│
├── webapp/                                     # ⭐ MASTER FULL-STACK MEAN APPLICATION (Q12, Q13, Q14)
│   ├── server.js                               # Express + Mongoose Backend API (GET, POST, PUT, DELETE)
│   └── public/
│       └── index.html                          # AngularJS SPA (Add, Edit, Delete & Dynamic Table)
│
├── webapp-nomng/                               # ⭐ FULL-STACK WEB APP WITHOUT MONGODB (IN-MEMORY ARRAY)
│   ├── server.js                               # Express REST API using in-memory array (No Mongo needed)
│   └── public/
│       └── index.html                          # AngularJS SPA (Add, Edit, Delete & Table)
│
├── webapp-validation/                          # ⭐ FULL-STACK EVENT MANAGEMENT WITH FORM VALIDATION
│   ├── server.js                               # Express + Mongoose Backend API (Event CRUD)
│   └── public/
│       └── index.html                          # AngularJS SPA with Real-time Form Validation
│
├── dependency/                                 # 📦 Local Vendor Dependencies
│   ├── angular.min.js                          # AngularJS v1.8.2 framework
│   └── bootstrap.min.css                       # Bootstrap v5.3.3 styling
│
├── package.json                                # Node dependencies & start script
└── README.md                                   # Master Syllabus Guide & Viva Bank
```

---

## 📑 Complete Journal Questions Mapping Table

### Part 1: Backend (MongoDB, Node.js & ExpressJS)

| Official Journal Practical Question | Single-File in `mean/` | Description & Non-Repeating Coverage |
| :--- | :--- | :--- |
| **Q1**: Create `schoolDB` and `students` collection; insert 5 documents (name, age, grade); queries: grade is A, insert multiple, update age of John, delete grade F, find all. | `01.js` | Complete MongoDB Shell script covering all 5 queries. |
| **Q2**: Employee schema with name, department, salary, experience. CRUD operations using Node.js & Mongoose. | `02.js` | Direct Mongoose operations (`create`, `find`, `updateOne`, `deleteOne`). |
| **Q3**: ExpressJS web server displaying "Welcome to ExpressJS" on homepage.<br>**Q4**: Configure routes for `/`, `/about`, and `/contact` with different responses. | `03.js` | **Consolidated**: Homepage serves the Welcome message, while `/about` and `/contact` demonstrate routing. |
| **Q5**: ExpressJS middleware to log request details (method, URL, time) and parse JSON input. | `04.js` | Custom logger middleware with `next()` and built-in `express.json()`. |
| **Q6**: Serve static resources (HTML, CSS, image) using `express.static()`. | `05.js` | Demonstrates `app.use(express.static(__dirname))` serving static assets. |
| **Q7**: RESTful API for student records (Add, View, Update, Delete using array).<br>**Q8**: REST API for Books collection (GET all, GET :id, POST, PUT, DELETE). | `06.js` | **Consolidated**: In-memory storage with full CRUD (GET all, GET by ID, POST, PUT, DELETE). |
| **Q9**: RESTful API in Node.js (Express) connected to MongoDB. | `07.js` | Express connected to Mongoose with full CRUD endpoints. |
| **Syllabus 4.3**: Pure Node.js HTTP web server. | `08.js` | Pure Node.js `http.createServer()` with routing and headers. |
| **Syllabus 4.2.1**: Node.js core modules (`fs`, `path`, `os`). | `09.js` | File creation, read, delete, path resolution, and OS platform info. |
| **Syllabus 4.2.2**: Node.js local module export and import. | `10.js` | Self-contained local module definition (`module.exports`) and execution. |

---

### Part 2: Frontend & Full-Stack (AngularJS & MEAN)

| Official Journal Practical Question | Single-File in `mean/` | Description & Non-Repeating Coverage |
| :--- | :--- | :--- |
| **Q1**: Take user's name and display welcome message.<br>**Q3**: Accept first and last name, display full name using expressions.<br>**Q6**: Accept name, age, city, display customized profile message. | `11.html` | **Consolidated**: Single inputs, string expressions (`{{ firstName + " " + lastName }}`), and complete profile card. |
| **Q2**: Accept number and display square and cube.<br>**Q7**: Accept number and display multiplication table. | `12.html` | **Consolidated**: Arithmetic expressions (`n*n`, `n*n*n`) and iterative table loop (`ng-repeat`). |
| **Q4**: Student marks in 3 subjects, calculate total and average.<br>**Q5**: Student name and marks, display pass or fail. | `13.html` | **Consolidated**: Computes total & average, dynamically displaying Pass/Fail with conditional styling. |
| **Q8**: Custom `<user-card>` directive.<br>**Q9**: Reusable `<student-card>` directive with `=` binding, pass/fail, view details button calling controller function via `&`. | `14.html` | **Consolidated**: Demonstrates both element directives, isolated scope with two-way data binding (`=`), and method execution (`&`). |
| **Q10**: User registration form with validation (required, name min 3, valid email, age 18-60, errors, disabled submit). | `15.html` | Complete form validation with `$dirty`, `$error`, `$invalid`, error messages, and success alert. |
| **Q11**: Simple Task Manager (To-Do App) web application (Add, View, Mark Complete, Delete). | `16.html` | In-memory task list with checkboxes, strikethrough class, add input, and delete splice. |
| **⭐ Q12, Q13, Q14**: Employee, Course & Event Management Systems | `webapp/` (`server.js` & `public/index.html`) | **Universal Full-Stack Application**: Covers complete CRUD (GET all, POST, PUT, DELETE) using the full Employee model schema (`employeeId`, `name`, `department`, `designation`, `email`, `salary`). |

---

## ⭐ High-Priority Exam Cheat Sheet (`webapp/`)

`webapp/` is the master exam program. It implements the complete CRUD lifecycle connecting **AngularJS -> ExpressJS -> MongoDB (Mongoose)**.

### 1. Backend: `webapp/server.js`
```javascript
const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());
app.use(express.static(__dirname + "/public"));
app.use(express.static(__dirname + "/../dependency"));

mongoose.connect("mongodb://127.0.0.1:27017/employeeDB");

const required = type => ({ type, required: true });

const Employee = mongoose.model("Employee", new mongoose.Schema({
  employeeId: { ...required(String), unique: true },
  name: required(String),
  department: required(String),
  designation: required(String),
  email: required(String),
  salary: required(Number)
}));

// Helper: wrap a route so any error becomes { error } with the given status
const handle = (errorCode, fn) => async (req, res) => {
  try { await fn(req, res); }
  catch (err) { res.status(errorCode).json({ error: err.message }); }
};

// CRUD routes
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
```

### 2. Frontend: `webapp/public/index.html` (Exam-Ready Snippet)
```html
<!DOCTYPE html>
<html lang="en" ng-app="employeeApp">
<head>
  <meta charset="UTF-8">
  <title>Employee Management System (MEAN)</title>
  <link rel="stylesheet" href="bootstrap.min.css">
  <script src="angular.min.js"></script>
</head>
<body class="bg-light" ng-controller="EmployeeController">
<div class="container py-4">
  <h2 class="mb-4">🏢 Employee Management System</h2>

  <div class="card card-body mb-4">
    <h4>{{ isEditing ? 'Edit Employee' : 'Add New Employee' }}</h4>
    <form class="row g-2" ng-submit="saveEmployee()">
      <div class="col-md-4"><input class="form-control" ng-model="form.employeeId" placeholder="Employee ID" ng-disabled="isEditing" required></div>
      <div class="col-md-4"><input class="form-control" ng-model="form.name" placeholder="Full Name" required></div>
      <div class="col-md-4"><input class="form-control" ng-model="form.department" placeholder="Department" required></div>
      <div class="col-md-4"><input class="form-control" ng-model="form.designation" placeholder="Designation" required></div>
      <div class="col-md-4"><input class="form-control" type="email" ng-model="form.email" placeholder="Email" required></div>
      <div class="col-md-4"><input class="form-control" type="number" ng-model="form.salary" placeholder="Salary" required></div>
      <div class="col-12">
        <button type="submit" class="btn btn-primary">{{ isEditing ? 'Update Employee' : 'Add Employee' }}</button>
        <button type="button" class="btn btn-secondary" ng-show="isEditing" ng-click="resetForm()">Cancel</button>
      </div>
    </form>
  </div>

  <div class="card card-body">
    <h4>All Employees</h4>
    <table class="table table-striped table-bordered" ng-if="employees.length > 0">
      <thead class="table-primary">
        <tr><th>ID</th><th>Name</th><th>Dept</th><th>Designation</th><th>Email</th><th>Salary</th><th>Actions</th></tr>
      </thead>
      <tbody>
        <tr ng-repeat="emp in employees">
          <td>{{ emp.employeeId }}</td><td>{{ emp.name }}</td><td>{{ emp.department }}</td>
          <td>{{ emp.designation }}</td><td>{{ emp.email }}</td><td>{{ emp.salary }}</td>
          <td>
            <button class="btn btn-warning btn-sm" ng-click="editEmployee(emp)">Edit</button>
            <button class="btn btn-danger btn-sm" ng-click="deleteEmployee(emp.employeeId)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

  <script>
    angular.module("employeeApp", [])
      .controller("EmployeeController", function($scope, $http) {
        var API = "/api/employees";
        $scope.employees = [];
        $scope.form = {};
        $scope.isEditing = false;

        function load() {
          $http.get(API).then(res => { $scope.employees = res.data; });
        }

        $scope.resetForm = () => { $scope.form = {}; $scope.isEditing = false; };

        $scope.saveEmployee = () => {
          var req = $scope.isEditing
            ? $http.put(API + "/" + $scope.form.employeeId, $scope.form)
            : $http.post(API, $scope.form);
          req.then(() => { $scope.resetForm(); load(); });
        };

        $scope.editEmployee = emp => { $scope.form = angular.copy(emp); $scope.isEditing = true; };

        $scope.deleteEmployee = id => {
          if (confirm("Delete employee " + id + "?")) {
            $http.delete(API + "/" + id).then(load);
          }
        };

        load();
      });
  </script>
</body>
</html>
```

---

## 🚀 How to Run

### 1. Install Node Dependencies
```bash
npm install
```

### 2. Run the Full-Stack Applications

#### Option A: With MongoDB (`webapp/`)
Make sure MongoDB is running locally (`mongod` or MongoDB Compass):
```bash
npm start
# or: node webapp/server.js
# Then open: http://localhost:3000
```

#### Option B: Without MongoDB (`webapp-nomng/` - In-Memory Array)
No MongoDB required! Ideal if MongoDB is not installed/running:
```bash
npm run start:nomng
# or: node webapp-nomng/server.js
# Then open: http://localhost:3000
```

#### Option C: Event Management with Form Validation (`webapp-validation/`)
MongoDB + Express + AngularJS with real-time client-side form validation:
```bash
npm run start:val
# or: node webapp-validation/server.js
# Then open: http://localhost:3000
```

### 3. Run Backend & Express APIs (`mean/`)
```bash
# 01: MongoDB Shell queries
mongosh < mean/01.js

# 02: Mongoose CRUD
node mean/02.js

# 03: Express Server & Routes
node mean/03.js

# 04: Middleware Logger
node mean/04.js

# 05: Static file serving
node mean/05.js

# 06: In-Memory REST API (CRUD)
node mean/06.js

# 07: MongoDB REST API
node mean/07.js

# 08: Pure Node.js HTTP Server
node mean/08.js

# 09: Node.js Core Modules
node mean/09.js

# 10: Node.js Local Module
node mean/10.js
```

### 4. Run AngularJS Practicals (`mean/`)
Every AngularJS file (`11.html` to `16.html`) is standalone and uses the AngularJS CDN. Simply **double-click any `.html` file** to open it directly in Chrome, Firefox, or Edge.

---

## 🎓 External Exam Viva Voce Questions & Answers

### Unit 1: MongoDB & Architecture
**Q1: What is the MEAN stack architecture?**
- **MongoDB**: NoSQL database that stores data in flexible, JSON-like BSON documents.
- **Express.js**: Fast, minimalist web framework for Node.js to build APIs and web servers.
- **AngularJS**: Client-side MVW framework providing two-way data binding and dependency injection.
- **Node.js**: Asynchronous, event-driven JavaScript server runtime.

**Q2: What is the difference between SQL and NoSQL?**
- SQL databases (MySQL, Oracle) use fixed schemas, tables, rows, and foreign keys.
- MongoDB uses dynamic schemas, collections, documents, and embeds or references data without joins.

---

### Unit 2: ExpressJS Framework
**Q3: What is Middleware and why is `next()` important?**
- Middleware functions execute during the request-response lifecycle before reaching route handlers.
- Calling `next()` passes control to the next middleware in line. Without `next()`, the request hangs.

**Q4: What are the REST HTTP methods?**
- `GET`: Read / retrieve data
- `POST`: Create new data
- `PUT`: Update existing data
- `DELETE`: Remove data

---

### Unit 3: AngularJS
**Q5: What is Two-Way Data Binding in AngularJS?**
- Synchronizes data between the Model and View automatically. When input changes in the View (`ng-model`), the Model updates instantly; when the Model changes, the View updates without manual DOM manipulation.

**Q6: What are custom directive scope symbols (`@`, `=`, `&`)?**
- `@`: One-way text binding (passes string values).
- `=`: Two-way data binding (binds directly to parent object).
- `&`: Method binding (calls parent controller function).

---

### Unit 4: NodeJS Fundamentals
**Q7: Explain the Node.js Event Loop.**
- Node.js is single-threaded and non-blocking. When an I/O task begins, Node offloads it to the system kernel or thread pool and continues. When done, a callback is queued and processed by the event loop, ensuring high concurrency.

**Q8: How do you create and export local modules?**
- Define functions on `module.exports` or `exports`:
  ```javascript
  exports.add = (a, b) => a + b;
  ```
- Import in another file using `require()`:
  ```javascript
  const calc = require("./calc");
  console.log(calc.add(2, 3));
  ```
