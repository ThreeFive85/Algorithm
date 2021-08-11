// https://programmers.co.kr/learn/courses/30/lessons/12982

const solution = (d, budget) => {
    let answer = 0;
    d.sort((a, b) => a - b);
    for(let i = 0; i < d.length; i++){
        if(d[i] > budget) break;
        budget -= d[i];
        answer += 1;
    }
    return answer;
}

export default solution;

// d.sort()는 d가 정렬되었다는 보장이 없어서 일부 테스트 케이스에서 실패가 된다.
// 따라서 d.sort((a, b) => a - b);가 필요하다.

// forEach문은 스코프 내에서 break, continue, return 등의 구문으로 함수를 벗어날 수 없다.
// SyntaxError: Illegal break statement 에러발생!
