/*
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42576
*/

const incompletePlayer = (participant, completion) => {
  //   participant.sort();
  //   completion.sort();

  //   for (let i = 0; i < participant.length; i++) {
  //     if (participant[i] !== completion[i]) {
  //       return participant[i];
  //     }
  //   }
  let answer = '';
  let myMap = new Map();

  for (let part of participant) {
    // console.log(part);
    if (!myMap.get(part)) {
      myMap.set(part, 1);
    } else {
      myMap.set(part, myMap.get(part) + 1);
    }
  }
  for (let com of completion) {
    if (myMap.get(com)) {
      myMap.set(com, myMap.get(com) - 1);
    }
  }
  for (let part of participant) {
    if (myMap.get(part) >= 1) {
      answer = part;
    }
  }
  //   console.log(myMap);
  console.log(answer);
  return answer;
};

export default incompletePlayer;

// incompletePlayer(
//   ['mislav', 'stanko', 'mislav', 'ana'],
//   ['stanko', 'ana', 'mislav'],
// );
