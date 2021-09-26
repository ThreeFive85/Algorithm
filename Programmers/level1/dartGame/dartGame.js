// https://programmers.co.kr/learn/courses/30/lessons/17682?language=javascript

export const solution = (dartResult) => {
    let bonus = { "S": 1, "D": 2, "T": 3};
    let options = { "*": 2, "#": -1, null: 1};
    let re = dartResult.match(/\d.?\D/g);
    let scoreArr = [];
    // console.log(re)
    re.forEach(el => {
        let num = Number(el.match(/[\d]+/g)[0]);
        let bon = el.match(/[SDT]/g)[0];
        let op = el.match(/[*#]/g);
        // console.log(`숫자 : ${num}, 보너스 : ${bon}, 옵션 : ${op}`)
        let score = Math.pow(num, bonus[bon]) * options[op];
        
        if(options[op] === 2){
            if(scoreArr.length === 0){
                scoreArr.push(score);
            } else {
                let pop = scoreArr.pop();
                scoreArr.push(pop * 2);
                scoreArr.push(score);
            }
        } else {
            scoreArr.push(score);
        }
    })
    // console.log(scoreArr)
    return scoreArr.reduce((a,b) => a + b);
}