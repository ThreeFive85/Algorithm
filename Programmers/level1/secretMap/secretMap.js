// https://programmers.co.kr/learn/courses/30/lessons/17681?language=javascript

export const solution = (n, arr1, arr2) => {
    let answer = [];
    for(let i = 0; i < arr1.length; i++){
        let a1 = bin(arr1[i], n);
        let a2 = bin(arr2[i], n);
        let str = ''
        for(let j = 0; j < a1.length; j++){
            if(a1[j] === '0' && a2[j] === '0'){
                str += ' ';
            } else {
                str += '#';
            }
        }
        answer.push(str)
    }
    return answer;
}

const bin = (arrIdx, n) => {
    let b = parseInt(arrIdx).toString(2);
    if(b.length < n){
        let len = n - b.length;
        let str = '0'.repeat(len);
        return str + b;
    };
    return b;
}