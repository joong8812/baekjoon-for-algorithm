let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = +input.shift();
const numbers = input[0].split(" ").map(Number);

const dp = new Array(N).fill(1);

// loop
for (let i = 1; i < N; i++) {
  let tmpMaxDp = [1];
  for (let j = 0; j < i; j++) {
    // 1. find a number under target number
    if (numbers[j] < numbers[i]) {
      // 2. push new dp max value to tmpMaxDp Array
      tmpMaxDp.push(1 + dp[j]);
    }
  }
  dp[i] = Math.max(...tmpMaxDp);
}

// 3. print max dp value
console.log(Math.max(...dp));
