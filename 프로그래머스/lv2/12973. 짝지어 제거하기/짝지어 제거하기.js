function solution(s) {
  const stack = [];

  for (char of s) {
    if (stack[stack.length - 1] === char) stack.pop();
    else stack.push(char);
  }
  return stack.length === 0 ? 1 : 0;
}

console.log(solution("cdcd"));
