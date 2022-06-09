let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const strToNumArr = (str) => str.split(' ').map(Number);
const drList = [1, -1, 0, 0];
const dcList = [0, 0, 1, -1];

const [C, R] = input.splice(0, 1)[0].split(' ').map(n => +n);
let tomatoCount = C * R, ripeCount = 0;

let prevRipeList = [];
const tomatoBox = input.map((str, r) => str.split(' ').map((state, c) => {
  const ret = +state;
  if (ret === -1) {
    tomatoCount--;
  }
  if (ret === 1) {
    prevRipeList.push(`${r} ${c}`);
    ripeCount++;
  }
  return ret;
}))

let day = 0;
const newRipeSet = new Set();
while (true) {
  prevRipeList.forEach(pos => {
    const [r, c] = strToNumArr(pos);

    drList.forEach((dr, i) => {
      const dc = dcList[i];
      nextR = r + dr;
      nextC = c + dc;

      if (nextR < 0 || nextR >= R || nextC < 0 || nextC >= C || tomatoBox[nextR][nextC] !== 0) return;

      tomatoBox[nextR][nextC] = 1;
      newRipeSet.add(`${nextR} ${nextC}`)
    })
  })

  if (newRipeSet.size === 0) break;
  
  day++;

  ripeCount += newRipeSet.size;
  prevRipeList = Array.from(newRipeSet);
  newRipeSet.clear();
}

console.log(ripeCount === tomatoCount ? day : -1);