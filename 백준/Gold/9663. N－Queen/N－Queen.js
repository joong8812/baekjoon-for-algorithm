let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

const chessTable = new Array(15)
let countCases = 0

const check = (row) => {
  for (let i = 0; i < row; i++) {
    if (chessTable[i] === chessTable[row] || Math.abs(chessTable[row] - chessTable[i]) === (row-i)) {
      return false;
    }
  }
  return true;
}

const nqueen = (nthQueen) => {
  if (nthQueen === totalQueens) {
    countCases++;
  } else {
    for (let i = 0; i < totalQueens; i++) {
      chessTable[nthQueen] = i;
      if (check(nthQueen)) nqueen(nthQueen+1)
    }
  }
}

const totalQueens = Number(input);
nqueen(0)
console.log(countCases);
