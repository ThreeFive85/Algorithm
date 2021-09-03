// https://programmers.co.kr/learn/courses/30/lessons/81301?language=javascript

export const solution = (s) => {
    let answer = s.replace(/zero/gi, '0')
    .replace(/one/gi, '1')
    .replace(/two/gi, '2')
    .replace(/three/gi, '3')
    .replace(/four/gi, '4')
    .replace(/five/gi, '5')
    .replace(/six/gi, '6')
    .replace(/seven/gi, '7')
    .replace(/eight/gi, '8')
    .replace(/nine/gi, '9')
    console.log(parseInt(answer));
    return parseInt(answer);
}

// s.replace(/zero/i, '0') 와 s.replace(/zero/gi, '0')의 차이는 
// solution("1zerotwozero3")일때 s.replace(/zero/i, '0')는 102고
// s.replace(/zero/gi, '0')는 10203으로 반복되는 문자들을 처리해준다.