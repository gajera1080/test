// Syllabus 4.2.1: NodeJS Core Modules (fs, path, os, url)
const fs = require("fs");
const path = require("path");
const os = require("os");

// 1. Path module: Safe path joining
const filePath = path.join(__dirname, "demo.txt");
console.log("File Path:", filePath);

// 2. OS module: System information
console.log("OS Platform :", os.platform());
console.log("Total Memory:", (os.totalmem() / 1e9).toFixed(2), "GB");

// 3. FS module: Synchronous Write & Read
fs.writeFileSync(filePath, "Hello from NodeJS Core fs module!");
const content = fs.readFileSync(filePath, "utf-8");
console.log("File Content:", content);

// Clean up demo file
fs.unlinkSync(filePath);
console.log("Demo file cleaned up successfully.");
