// ============================================================
// PRACTICAL 1: MongoDB Shell Commands (schoolDB & students)
// How to run: mongosh < mean/01.js (or paste in mongosh)
// ============================================================

// 1. Switch or Create Database
use schoolDB

// 2. Insert 5 Initial Student Documents with fields: name, age, grade
db.students.insertMany([
  { name: "John", age: 19, grade: "B" },
  { name: "Alice", age: 20, grade: "A" },
  { name: "Bob", age: 21, grade: "A" },
  { name: "Charlie", age: 18, grade: "C" },
  { name: "David", age: 22, grade: "F" }
])

// ------------------------------------------------------------
// MANDATORY PRACTICAL QUERIES
// ------------------------------------------------------------

// Query 1: Fetch all students whose grade is 'A'
db.students.find({ grade: "A" })

// Query 2: Insert multiple documents into collection
db.students.insertMany([
  { name: "Emma", age: 20, grade: "A" },
  { name: "Frank", age: 19, grade: "B" }
])

// Query 3: Update the age of a student where name = 'John'
db.students.updateOne(
  { name: "John" },
  { $set: { age: 23 } }
)

// Query 4: Delete a document where grade = 'F'
db.students.deleteOne({ grade: "F" })

// Query 5: Find all documents from collection
db.students.find()
