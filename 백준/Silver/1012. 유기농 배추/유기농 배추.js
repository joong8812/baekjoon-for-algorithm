let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const T = +input.shift();
let testCase = 0;

const distance = [[-1, 0], [1, 0], [0, -1], [0, 1]];
let M, N, K, ground;

const bfs = (rStart, cStart) => {
  const queue = [[rStart, cStart]];
  let currentR, currentC, r, c;

  while (queue.length !== 0) {
    [currentR, currentC] = queue.shift();

    if (!ground[currentR][currentC]) continue;

    ground[currentR][currentC] = 0;
    distance.forEach(([dr, dc]) => {
      r = currentR + dr;
      c = currentC + dc;
      if (r < 0 || r>=N || c < 0 || c>=M) return;
      if (ground[r][c]) {
        queue.push([r, c]);
      }
    })
  }
}

while (testCase < T){
  [M, N, K] = input.shift().split(' ').map(n => +n);
  ground = [...Array(N)].map(() => Array(M).fill(0));
  let countNeedBugs = 0;

  for (let i = 0; i < K; i++) {
    const [c, r] = input.shift().split(' ').map(n => +n);
    ground[r][c] = 1;
  }

  while (true) {
    let r, c;

    for (let i = 0; i<N; i++) {
      const j = ground[i].indexOf(1);

      if (j === -1) continue;

      r = i;
      c = j;
      break;
    }

    if (r === undefined && c === undefined) break;

    countNeedBugs++;
    bfs(r, c);
  }
  console.log(countNeedBugs);
  
  testCase++;
}

