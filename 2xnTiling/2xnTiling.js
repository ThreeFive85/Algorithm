/**
 *  문체 출처 : https://programmers.co.kr/learn/courses/30/lessons/12900
 */

const solution = (n) => {
  let answer = 0;
  let left = 0;
  let right = 1;
  let temp;
  let m = 1000000007;

  for (let i = 2; i <= n; i++) {
    temp = (left + right) % m;
    left = right;
    right = temp;
  }
  answer = (left + right) % m;
  return answer;
};

export default solution;
