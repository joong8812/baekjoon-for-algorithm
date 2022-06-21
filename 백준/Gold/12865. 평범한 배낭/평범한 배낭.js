let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, K] = input.shift().split(' ').map(n => +n);
const belongings = input.map(stuff => stuff.split(' ').map(n => +n));
belongings.unshift(undefined);

const maxVSum = [];
for (let i = 0; i <= N; i++) {
  maxVSum.push(Array(K+1).fill(0));
}

for (let i = 1; i <= N; i++) {
  const [weight, value] = belongings[i];
  for (let j = 0; j <= K; j++) {
    if (j < weight) {
      maxVSum[i][j] = maxVSum[i - 1][j];
    } else {
      maxVSum[i][j] = Math.max(maxVSum[i - 1][j], maxVSum[i - 1][j-weight] + value)
    }
  }
}

console.log(maxVSum[N][K])