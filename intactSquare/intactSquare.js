/**
 * 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/62048
 */

const solution = (w, h) => {
  let gcd = 1;
  let min = Math.min(w, h);

  for (let i = min; min > 0; i--) {
    if (w % i === 0 && h % i === 0) {
      gcd = i;
      break;
    }
  }
  return w * h - (w + h - gcd);
};

export default solution;
