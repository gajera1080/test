// ============================================================
// 10: NodeJS Local Modules (Exporting and Importing)
// ============================================================

// 1. Defining and Exporting a Local Module (Equivalent to calc.js)
const calcModule = {
  add: (a, b) => a + b,
  sub: (a, b) => a - b,
  mul: (a, b) => a * b
};

// In a separate file (e.g. calc.js), you write:
// module.exports = calcModule;
// or:
// exports.add = (a, b) => a + b;

// 2. Importing and Using the Local Module (Equivalent to app.js)
// In a separate file (e.g. app.js), you write:
// const calc = require("./calc");
const calc = calcModule;

console.log("=== Node.js Local Module Demo ===");
console.log("Add 10 + 5 :", calc.add(10, 5));
console.log("Sub 10 - 5 :", calc.sub(10, 5));
console.log("Mul 10 * 5 :", calc.mul(10, 5));
