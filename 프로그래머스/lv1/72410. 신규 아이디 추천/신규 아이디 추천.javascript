function solution(new_id) {
    var answer = '';
    let strChanging = ''; 
    // step1. Capital -> small
    strChanging = new_id.toLowerCase();
    
    // step2. eliminate except small, digits, -, _, .
    const regStep2 = /[\w\-\.]/g;
    strChanging = strChanging.match(regStep2).join('');
    
    // step3. dot continues over 2 -> one dot
    const regStep3 = /\.{2,}/g;
    strChanging = strChanging.replace(regStep3, '.');
    
    // step4. eliminate the dots if it's in front of string or in end of string.
    if (strChanging[0] === '.') strChanging = strChanging.slice(1);
    if (strChanging[strChanging.length - 1] === '.') strChanging = strChanging.slice(0, -1);
    
    // step5. null -> a
    if (strChanging === null || strChanging.length === 0) {
        strChanging = 'a'
    } else {
        const regStep5 = /\s/g;
        strChanging = strChanging.replace(regStep5, 'a');    
    }
    
    // step6. make string length 15
    if (strChanging.length >= 16) strChanging = strChanging.slice(0,15);
    if (strChanging[strChanging.length - 1] === '.' && strChanging.length === 15) {
        strChanging = strChanging.slice(0, -1);
    }
    
    // step7. if string length is less equal than 2, add the last letter until make lnegth 3
    let strLength = strChanging.length;
    if (strLength <= 2) {
        const lastLetter = strChanging[strLength -1];
        for (let i = 0; i < 3 - strLength; i++) {
            strChanging += lastLetter;
        }
    }
    answer = strChanging;
    return answer;
}