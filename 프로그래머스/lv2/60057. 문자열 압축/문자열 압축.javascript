function solution(s) {
  let answer = s.length;
  
  for (let i = 1; i <= parseInt(s.length/2) + 1; i++) {
    let tempArr = [];
    let pos = 0;

    while(pos < s.length) {
      tempArr.push(s.slice(pos, pos+i))
      pos += i;
    }

    let count = 1;
    let newString = "";
    
    for (let j = 0; j < tempArr.length; j++) {
      if (j === 0) {
        newString += tempArr[j];
        continue;
      }

      if (tempArr[j-1] === tempArr[j]) {
        // if (count !== 0) continue;
        count++;
      } else {
        if (count !== 1) newString += count;
        count = 1;
        newString += tempArr[j]
      }
    }

    if (count !== 1) newString += count;
    
    answer = Math.min(answer, newString.length);
    tempArr = [];
  }
  return answer;
}