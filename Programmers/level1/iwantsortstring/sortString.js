// https://programmers.co.kr/learn/courses/30/lessons/12915?language=javascript

export const solution = (strings, n) => {
    let answer = strings.sort((a,b) => {
        if(a[n] > b[n]) return 1;
        if(a[n] < b[n]) return -1;
        else { // 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치
            if(a > b) return 1;
            if(a < b) return -1;
        }
        return 0;
    });
    // console.log(answer)
    return answer;
}