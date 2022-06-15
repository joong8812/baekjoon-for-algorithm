let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = input.map(n => +n);

let left = 1;
let right = n * n;
let result = 0;

while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  let count = 0;

  for (let i =1; i<=n; i++) {
    count += Math.min(n, Math.floor(mid / i));
  }

  if (count >= k) {
    result = mid;
    right = mid - 1;
  } else {
    left = mid + 1;
  }
}

console.log(result);