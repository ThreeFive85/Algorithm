// https://programmers.co.kr/learn/courses/30/lessons/12924?language=javascript

export const solution = (n) => {
    var answer = 1;
    for(let i = 1; i < parseInt(n/2)+2; i++){
        let sum = i;
        for(let j = i+1; i < parseInt(n/2)+2; j++){
            sum += j;
            if(sum === n){
                answer += 1;
                break;
            }
            if(sum > n){
                break;
            } else {
                continue;
            }
        }
    }
    return answer;
}