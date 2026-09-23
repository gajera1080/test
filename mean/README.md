# MEAN Stack Practicals

This directory contains complete implementations for the 9 MEAN stack practical programs.

## Prerequisites
- Node.js (v16+)
- MongoDB (Running locally on `mongodb://127.0.0.1:27017` or via MongoDB Atlas URI in `MONGODB_URI` environment variable)

## Setup
```bash
cd mean
npm install
```

---

## Programs Summary

### 1. MongoDB Queries (`1_mongodb_queries.js`)
- Database: `schoolDB`, Collection: `students`.
- Inserts 5 student documents with `name`, `age`, and `grade`.
- Demonstrates:
  1. Fetch all students whose grade is `A`.
  2. Insert multiple documents into collection.
  3. Update age of student where `name = "John"`.
  4. Delete document where `grade = "F"`.
  5. Find all documents from collection.
- **Run:** `node 1_mongodb_queries.js` or directly inside `mongosh`.

### 2. Employee Schema & CRUD using Mongoose (`2_employee_crud_mongoose.js`)
- Mongoose Schema with `name`, `department`, `salary`, `experience`.
- Complete CRUD functions: `createEmployee()`, `getAllEmployees()`, `updateEmployee()`, `deleteEmployee()`.
- **Run:** `node 2_employee_crud_mongoose.js`

### 3. ExpressJS Welcome Page (`3_express_welcome.js`)
- Starts web server on port 3000 and displays "Welcome to ExpressJS" at `/`.
- **Run:** `node 3_express_welcome.js`
- **Test:** Open `http://localhost:3000/` in browser.

### 4. ExpressJS Multi-Route Server (`4_express_routes.js`)
- Configured routes for `/`, `/about`, and `/contact` with distinct responses and navigation links.
- **Run:** `node 4_express_routes.js`
- **Test:**
  - `http://localhost:3000/`
  - `http://localhost:3000/about`
  - `http://localhost:3000/contact`

### 5. ExpressJS Middleware (`5_express_middleware.js`)
- Custom logger middleware logging HTTP method, URL, and timestamp.
- JSON body parsing via `express.json()`.
- **Run:** `node 5_express_middleware.js`
- **Test:**
  - `GET http://localhost:3000/`
  - `POST http://localhost:3000/api/user` with JSON body `{"name": "Alice", "email": "alice@example.com"}`

### 6. ExpressJS Static File Serving (`6_express_static.js`)
- Serves static resources (`index.html`, `style.css`, and `logo.svg`) from `public/` directory via `express.static()`.
- **Run:** `node 6_express_static.js`
- **Test:** Open `http://localhost:3000/` in browser.

### 7. Student RESTful API with In-Memory Array (`7_student_rest_api_array.js`)
- In-memory array CRUD for student records.
- **Endpoints:**
  - `GET /students` - View all students
  - `GET /students/:id` - View student by ID
  - `POST /students` - Add new student
  - `PUT /students/:id` - Update student
  - `DELETE /students/:id` - Delete student
- **Run:** `node 7_student_rest_api_array.js`

### 8. Books Collection REST API (`8_books_rest_api.js`)
- Specific REST API endpoints:
  - `GET /books` → Get all books
  - `GET /books/:id` → Get a book by ID
  - `POST /books` → Add a new book
  - `PUT /books/:id` → Update a book by ID
  - `DELETE /books/:id` → Delete a book by ID
- **Run:** `node 8_books_rest_api.js`

### 9. Express RESTful API Connected to MongoDB (`9_mongodb_rest_api.js`)
- Connects to MongoDB database using Mongoose.
- Full persistent CRUD endpoints for `Product` collection:
  - `GET /api/products`
  - `GET /api/products/:id`
  - `POST /api/products`
  - `PUT /api/products/:id`
  - `DELETE /api/products/:id`
- **Run:** `node 9_mongodb_rest_api.js`
