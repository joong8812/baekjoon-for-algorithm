let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let readLineIndex = 0;
const readInput = () => input[readLineIndex++];

const memo = Array.from(Array(21), () => Array.from(Array(21), () => Array(21).fill(0)));

const w = (a, b, c) => {
  if (a <= 0 || b <= 0 || c <= 0) return 1;
  if (a > 20 || b > 20 || c > 20) return w(20, 20, 20);

  if (memo[a][b][c] !== 0) return memo[a][b][c];

  if (a < b && b < c) {
    const t1 = memo[a][b][c-1] = w(a, b, c-1);
    const t2 = memo[a][b-1][c-1] = w(a, b-1, c-1);
    const t3 = memo[a][b-1][c] = w(a, b-1, c);
    return memo[a][b][c] = t1 + t2 - t3;
  }

  const t1 = memo[a-1][b][c] = w(a-1, b, c);
  const t2 = memo[a-1][b-1][c] = w(a-1, b-1, c);
  const t3 = memo[a-1][b][c-1] = w(a-1, b, c-1);
  const t4 = memo[a-1][b-1][c-1] = w(a-1, b-1, c-1);
  
  return memo[a][b][c] = t1 + t2 + t3 - t4;
};


while(true) {
  let [a, b, c] = readInput().split(" ");
  a = +a;
  b = +b;
  c = +c;
  if (a === -1 && b === -1 && c === -1) break;
  console.log(`w(${a}, ${b}, ${c}) = ${w(a, b, c)}`);
}
