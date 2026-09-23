// 1. Create database and collection, insert 5 students
use schoolDB;

db.students.insertMany([
  { name: "John", age: 15, grade: "B" },
  { name: "Sarah", age: 14, grade: "A" },
  { name: "Mike", age: 16, grade: "A" },
  { name: "Emma", age: 15, grade: "C" },
  { name: "David", age: 14, grade: "F" }
]);

// 1. Fetch students with grade A
db.students.find({ grade: "A" });

// 2. Insert multiple documents
db.students.insertMany([
  { name: "Alice", age: 15, grade: "A" },
  { name: "Bob", age: 16, grade: "B" }
]);

// 3. Update age of John
db.students.updateOne({ name: "John" }, { $set: { age: 16 } });

// 4. Delete document with grade F
db.students.deleteOne({ grade: "F" });

// 5. Find all documents
db.students.find();
