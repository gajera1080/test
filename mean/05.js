// ============================================================
// 05: ExpressJS Serve Static Resources (express.static)
// ============================================================
const express = require("express");
const path = require("path");
const app = express();

// Serve all static files in current directory (.html, .css, .js)
app.use(express.static(__dirname));

// Default demo route
app.get("/", (req, res) => {
  res.send(`
    <div style="font-family: Arial; padding: 20px;">
      <h2 style="color: #007bff;">Express.js Static Resource Server</h2>
      <p>Serving static files via <code>express.static(__dirname)</code>.</p>
      <ul>
        <li><a href="/11.html">11.html (Expressions & Profile)</a></li>
        <li><a href="/12.html">12.html (Numbers & Tables)</a></li>
        <li><a href="/13.html">13.html (Marks & Pass/Fail)</a></li>
        <li><a href="/14.html">14.html (Custom Directives)</a></li>
        <li><a href="/15.html">15.html (Form Validation)</a></li>
        <li><a href="/16.html">16.html (To-Do App)</a></li>
      </ul>
    </div>
  `);
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Static server running at http://localhost:${PORT}`));
