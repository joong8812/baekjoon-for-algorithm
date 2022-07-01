function solution(numbers) {
    var answer = -1;
    let sum = 0;
    for (let num of numbers) sum += num;
    answer = 45 - sum;
    return answer;
}