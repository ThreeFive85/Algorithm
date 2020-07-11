/*
 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42588
 */

const solution = (heights) => {
  return heights.map((item, idx) => {
    while (idx >= 0) {
      idx--;
      if (heights[idx] > item) {
        return idx + 1;
      }
    }
    return 0;
  });
};

export default solution;
