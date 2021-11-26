// https://programmers.co.kr/learn/courses/30/lessons/67257?language=javascript
// 참고 블로그 : https://yoon-dumbo.tistory.com/entry/프로그래머스-수식-최대화-javascript

export const solution = (expression) => {
    const permut = [
        ['*', '+', '-'],
        ['*', '-', '+'],
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
    ]
    let result = [];
    for(let op of permut){
        // ex) op = ['*', '+', '-']
        const temp = expression.split(/(\D)/)
        // temp = ["100", "-", "200", "*", "300", "-", "500", "+", "20"]
        for(let o of op){
            // ex ) o = '*'
            while(temp.includes(o)){
                // 현재 temp에 "*"가 있으니
                let idx = temp.indexOf(o);
                // '*'의 인덱스를 저장
                temp.splice(idx-1, 3, eval(temp.slice(idx-1, idx+2).join('')))
                // "200", "*", "300"를 slice로 자른 뒤 "200*300"으로 조인한 뒤 
                // eval로 문자열 계산을 하고 그 결과를 splice로 60000을 추가
                // temp = ["100", "-", "60000", "-", "500", "+", "20"]
            }
            // 그 다음인 op의 '+'를 위의 과정으로 반복
        }
        // 모든 op의 내용을 반복한 뒤 최종 결과 값을 result에 절대값으로 넣음
        result.push(Math.abs(temp[0]))
    }
    console.log(result)
    return Math.max(...result);
}
