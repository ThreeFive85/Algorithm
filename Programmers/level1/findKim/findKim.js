// https://programmers.co.kr/learn/courses/30/lessons/12919?language=javascript

export const solution = (seoul) => {
    let answer = `김서방은 ${seoul.indexOf('Kim')}에 있다`;
    if(seoul.indexOf('Kim') === -1) return '김서방은 존재하지 않는다';
    return answer;
}