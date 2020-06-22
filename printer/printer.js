/*
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42587
입출력 예
priorities	            location	         return
[2, 1, 3, 2]	           2	               1
[1, 1, 9, 1, 1, 1]	       0	               5
*/

const printer = (priorities, location) => {
  let count = 1;
  let targer_index = location;
  let first;

  while (priorities.length > 0) {
    first = priorities.shift();
    if (priorities.some((value, idx) => value > first)) {
      priorities.push(first);
    } else {
      if (targer_index === 0) {
        break;
      } else {
        count++;
      }
    }
    if (targer_index === 0) {
      targer_index = priorities.length - 1;
    } else {
      targer_index--;
    }
  }
  return count;
};

export default printer;
