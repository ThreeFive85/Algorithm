// https://programmers.co.kr/learn/courses/30/lessons/76502?language=javascript

export const solution = (s) => {
    let answer = 0;
    let cnt = s.length;
    while(cnt > 0){
        if(check(s)){
            answer += 1;
        };
        s = s.slice(1) + s.slice(0,1);
        cnt -= 1;
    }
    return answer;
}

const check = (input) => {
  let stackArr = [];
  let strObj = {
    '(': ')',
    '{': '}',
    '[': ']',
  };

  for (let i = 0; i < input.length; i++) {
    if (input[i] === '(' || input[i] === '{' || input[i] === '[') {
      stackArr.push(input[i]);
    } else if (input[i] === ')' || input[i] === '}' || input[i] === ']') {
      let resent = stackArr.pop();
      if (input[i] !== strObj[resent]) {
        return false;
      }
    }
  }

  if (stackArr.length !== 0) {
    return false;
  } else {
    return true;
  }
};