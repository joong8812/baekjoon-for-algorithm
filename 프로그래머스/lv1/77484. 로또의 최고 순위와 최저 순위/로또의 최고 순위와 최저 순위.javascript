function solution(lottos, win_nums) {
    var answer = [];
    const rank = [6, 5, 4, 3, 2];
    let countMatchingNum = 0;
    let amountZero = 0;
    
    for (let num of win_nums) {
        if (lottos.includes(num)) countMatchingNum += 1;
    }
    
    // Lowest Rank
    if (countMatchingNum < 2) {
        answer[1] = 6;    
    } else {
        answer[1] = rank.indexOf(countMatchingNum) + 1;
    }
    
    // Highest Rank
    for (let num of lottos) {
        if (num === 0) amountZero++;
    }
    answer[0] = rank.indexOf(countMatchingNum + amountZero) + 1;
    if (answer[0] === 0) answer[0] = 6;
    
    return answer;
}