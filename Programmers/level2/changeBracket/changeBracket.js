export const solution = (p) => {
    var answer = '';
    
    while(p.length !== 0){
        let u = divide(p)[0];
        p = divide(p)[1] ;
        // console.log('u : ', u);
        // console.log('p : ', p)
        if(check(u)){
            answer += u
        } else {
            answer += '(' + solution(p) + ')' + reverse(u.slice(1,-1))
            break
        }
    }
    return answer;
}

const divide = (p) => {
    let cnt = [0, 0]
    for(let i = 0; i < p.length; i++){
        if(p[i] === '('){
            cnt[0] += 1;
        }else{
            cnt[1] += 1;
        }
        if(cnt[0] === cnt[1]){
            break;
        }
    }
    let sum = cnt[0] + cnt[1];
    let result = [p.slice(0,sum), p.slice(sum,)]
    return result
}

const check = (s) => {
    let stack = [];
    for(let i = 0; i < s.length; i++){
        if(s[i] === '('){
            stack.push(')');
        }
        if(s[i] === ')'){
            if(stack.length === 0){
                return false
            }
            stack.pop()
        }
    return true;
    }
}

const reverse = (v) => {
    let temp = '';
    for(let i = 0; i < v.length; i++){
        if(v[i] === '('){
            temp += ')';
        } else {
            temp += '(';
        }
    }
    return temp;
}