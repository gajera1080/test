// Consolidated Practicals 3 & 4: ExpressJS Web Server & Routing (/, /about, /contact)
const express = require("express");
const app = express();

// Practical 3: Welcome message on Homepage
app.get("/", (req, res) => {
  res.send("Welcome to ExpressJS");
});

// Practical 4: Route configuration for /about and /contact
app.get("/about", (req, res) => {
  res.send("About Page: Learning MEAN Stack (MongoDB, Express, Angular, Node)");
});

app.get("/contact", (req, res) => {
  res.send("Contact Page: Reach us at contact@university.edu");
});

app.listen(3000, () => {
  console.log("Express Server running at http://localhost:3000");
});
