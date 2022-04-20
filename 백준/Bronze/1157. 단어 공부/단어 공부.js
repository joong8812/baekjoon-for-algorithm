const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.on("line", function (line) {
    input = line.toLowerCase()
}).on("close", function () {
    let aToz = new Array(26).fill(0)
    let maxNum = maxIndex = maxDuple = 0;
    for (let letter of input) {
        aToz[letter.charCodeAt()-97] += 1;
    }
    for (let i = 0; i < aToz.length; i++) {
        if (aToz[i] > maxNum) {
            maxNum = aToz[i];
            maxIndex = i;
            maxDuple = 0
        } else if (aToz[i] === maxNum) {
            maxDuple++;
        }
    }
    if (maxDuple > 0) { console.log('?') }
    else { console.log(String.fromCharCode(maxIndex+65))}
    process.exit();
});