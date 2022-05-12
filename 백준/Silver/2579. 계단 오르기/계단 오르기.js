let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

[n, ...stairs] = input;
n = Number(n);
stairs = stairs.map((i) => Number(i));

const dp = new Array(n).fill(0);
dp[0] = stairs[0];
dp[1] = Math.max(stairs[0] + stairs[1], stairs[1]);
dp[2] = Math.max(stairs[0] + stairs[2], stairs[1] + stairs[2]);

const solution = (n, stairs, dp) => {
  for (let i = 3; i < n; i++) {
    dp[i] = Math.max(stairs[i] + stairs[i - 1] + dp[i - 3], stairs[i] + dp[i - 2]);
  }
  console.log(dp[n - 1]);
};

solution(n, stairs, dp);