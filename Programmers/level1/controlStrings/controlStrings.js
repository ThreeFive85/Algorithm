// https://programmers.co.kr/learn/courses/30/lessons/12918?language=javascript

export const solution = (s) => {
    if(s.length === 4 || s.length === 6){
        if(s.includes('e')) return false;
        if(Number(s)) return true;
        return false;
    } else {
        return false;
    }
}

// Number 함수는 e도 숫자로 변환하여 지수로 계산