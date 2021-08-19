// https://programmers.co.kr/learn/courses/30/lessons/77884?language=javascript

export const solution = (left, right) => {
    let answer = 0;
    for(let j = left; j < right+1; j++){
        let num = divisorCnt(j);
        if(num % 2 === 0){
            answer += j;
        } else {
            answer -= j;
        }
    }
    return answer;
}

const divisorCnt = (num) => {
    let cnt = 0
    for(let i = 1; i < num+1; i++){
        if(num % i === 0){
            cnt += 1;
        }
    }
    return cnt
}
