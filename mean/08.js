// Syllabus 4.3: Creating a Pure NodeJS Web Server using Core 'http' Module
const http = require("http");

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Welcome to NodeJS Web Server!");
  } else if (req.url === "/about") {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("About NodeJS: High performance asynchronous event-driven JavaScript runtime.");
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Page Not Found");
  }
});

server.listen(3000, () => {
  console.log("NodeJS Core HTTP Server running at http://localhost:3000");
});
