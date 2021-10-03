// https://programmers.co.kr/learn/courses/30/lessons/82612?language=javascript

export const solution = (price, money, count) => {
    let answer = 0;
    let cnt = 1;
    while(cnt < count+1){
        let pri = price * cnt;
        answer += pri;
        cnt += 1;
    };
    if(answer - money > 0){
        return answer - money;
    } else {
        return 0;
    };
};