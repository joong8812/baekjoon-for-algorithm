let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, ...costs] = input;
n = +n;
costs = costs.map(i => i.split(' ').map(i => +i));


for (let i=1; i<n; i++) {
  costs[i][0] += Math.min(costs[i-1][1], costs[i-1][2]);
  costs[i][1] += Math.min(costs[i-1][0], costs[i-1][2]);
  costs[i][2] += Math.min(costs[i-1][0], costs[i-1][1]);
}

console.log(Math.min(...costs[n-1]));