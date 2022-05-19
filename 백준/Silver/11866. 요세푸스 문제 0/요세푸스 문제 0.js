let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

const [n, k] = input;
let yosepus = [];
let initCircle = [];

for (let i = 1; i < +n + 1; i++) {
  initCircle.push(i);
}

while(true){
  let totalPeople = initCircle.length;
  if (totalPeople === 0) break;

  let exitPersonNum = 0;
  for (let i =0; i<k; i++) {
    exitPersonNum = initCircle.shift();
    if (i === k-1) break;

    initCircle.push(exitPersonNum);
  }  
  yosepus.push(exitPersonNum)
}

console.log(`<${yosepus.join(', ')}>`)