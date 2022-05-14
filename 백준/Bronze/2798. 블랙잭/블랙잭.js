const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const NM = input
  .shift()
  .split(" ")
  .map((num) => parseInt(num));
const N = NM.shift();
const M = NM.shift();
const cardArr = input
  .shift()
  .split(" ")
  .map((num) => parseInt(num));
let max = 0;

for (let i = 0; i < N - 2; i++) {
  for (let j = i + 1; j < N - 1; j++) {
    for (let k = j + 1; k < N; k++) {
      let sum = cardArr[i] + cardArr[j] + cardArr[k];
      if (sum > max && sum <= M) {
        max = sum;
      }
    }
  }
}

console.log(max);