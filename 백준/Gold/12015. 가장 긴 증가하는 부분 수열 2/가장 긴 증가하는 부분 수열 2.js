let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const binarySearch = (result, input, i) => {
  let left = 0;
  let right = result.length - 1;

  while (left < right) {
      const mid = parseInt((left + right) / 2);
      if (result[mid] < input[i]) {
          left = mid + 1;
      } else if (result[mid] > input[i]) {
          right = mid;
      } else {
          return mid;
      }
  }
  return right;
}

const n = +input.shift();
input = input[0].split(' ').map(n => +n)
const result = [input[0]];

for (let i = 1; i < n; i++) {
    if (result[result.length - 1] < input[i]) {
        result.push(input[i]);
        continue;
    }

    const idx = binarySearch(result, input, i);
    result[idx] = input[i];
}

console.log(result.length);