let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [t, ...testCases] = input;

testCases = testCases.map(n => +n);

let memo = new Array(90).fill(0);
memo = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, ...memo];

const p = (n) => {
  if (memo[n] !== 0) return memo[n];
  return memo[n] = p(n-1) + p(n-5);
}

for (let i =0; i < +t; i++) {
  console.log(p(testCases[i]));
}