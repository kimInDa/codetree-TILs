const fs = require("fs");

let input = fs.readFileSync(0).toString().split(' ').map(Number)

console.log(input[2] + input[4] + input[9])