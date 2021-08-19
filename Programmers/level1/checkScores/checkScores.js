// https://programmers.co.kr/learn/courses/30/lessons/83201?language=javascript

export const solution = (scores) => {
    let answer = '';
    for(let i = 0; i < scores.length; i++){
        let tmp = [];
        let student_score = scores[i][i];
        for(let j = 0; j < scores.length; j++){
            tmp.push(scores[j][i]);
        }
        if(Math.max(...tmp) === student_score && tmp.filter(e => e === student_score).length === 1){
            const idx = tmp.indexOf(student_score);
            tmp.splice(idx, 1);
        }
        if(Math.min(...tmp) === student_score && tmp.filter(e => e === student_score).length === 1){
            const idx = tmp.indexOf(student_score);
            tmp.splice(idx, 1);
        }
        // console.log(tmp)
        let avg = tmp.reduce((prev, curr) => (prev + curr)) / tmp.length;
        if(avg >= 90){
            answer += 'A'
        } else if(avg >= 80){
            answer += 'B'
        } else if(avg >= 70){
            answer += 'C'
        } else if(avg >= 50){
            answer += 'D'
        } else {
            answer += 'F'
        }
    }
    return answer;
}