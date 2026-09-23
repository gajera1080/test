const express = require("express");
const app = express();

// Parse JSON input
app.use(express.json());

// Logger middleware
app.use((req, res, next) => {
  console.log(`[${new Date().toLocaleTimeString()}] ${req.method} ${req.url}`);
  next();
});

app.post("/data", (req, res) => {
  res.json({ message: "Data received", data: req.body });
});

app.listen(3000, () => console.log("Server running on port 3000"));
