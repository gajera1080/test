// Practical 5: ExpressJS Middleware (Request Logger & JSON Input Parser)
const express = require("express");
const app = express();

// 1. Built-in JSON body parser middleware
app.use(express.json());

// 2. Custom Logger Middleware: Logs Method, URL, and Time
app.use((req, res, next) => {
  console.log(`[${new Date().toLocaleTimeString()}] ${req.method} ${req.url}`);
  next(); // Pass control to the next handler
});

app.get("/", (req, res) => {
  res.send("Middleware Logger Active. View terminal for logs!");
});

app.post("/data", (req, res) => {
  res.json({ status: "Success", received: req.body });
});

app.listen(3000, () => {
  console.log("Middleware server running at http://localhost:3000");
});
