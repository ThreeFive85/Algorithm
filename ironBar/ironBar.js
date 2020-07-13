/*
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42585
*/

const solution = (arrangement) => {
  let answer = 0;
  let stack = [];

  for (let i = 0; i < arrangement.length; i++) {
    if (arrangement[i] === '(') {
      stack.push('(');
    } else {
      stack.pop();
      if (arrangement[i - 1] === '(') {
        answer += stack.length;
      } else {
        answer += 1;
      }
    }
  }
  return answer;
};

export default solution;
