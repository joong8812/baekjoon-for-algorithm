function solution(board, moves) {
    const bucket = [];
    let countDisappearedDolls = 0;
    
    // moves iteration
    for(let move of moves) {
        for(let row of board) {
            let pickedNumber = row[move-1];
            row[move-1] = 0;
            
            if(!pickedNumber) {
                continue;
            }
            
            // pop a nth doll and move into a bucket
            let countInsideOfBucket = bucket.length;
            if(countInsideOfBucket !== 0) {
                // check if a doll can be disappear with below a doll.
                if(bucket[countInsideOfBucket - 1] === pickedNumber) {
                    bucket.pop();
                    // count disappeared dolls
                    countDisappearedDolls += 2;
                    break;
                }
            } 
            bucket.push(pickedNumber);
            break;
        }
    }
    return countDisappearedDolls;
}

/*
0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1

1 5 3 5 1 2 1 4
4 3 1 1 3 2 0 4 
*/