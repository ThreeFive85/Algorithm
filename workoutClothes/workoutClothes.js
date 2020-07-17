/**
 * 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42862
 */

const solution = (n, lost, reserve) => {
  // 맨 처음 초기상태로 모든 학생이 체육복이 있는 경우로 배열을 1로 채운다
  const student = Array(n).fill(1);

  // 체육복을 잃어버린 학생은 -1을 한다.
  for (let i = 0; i < lost.length; i++) {
    const index = lost[i] - 1;
    student[index]--;
  }

  // 여벌의 체육복을 가진 학생은 +1을 한다.
  for (let i = 0; i < reserve.length; i++) {
    const index = reserve[i] - 1;
    student[index]++;
  }

  for (let i = 0; i < student.length; i++) {
    // 맨 첫번째 학생이 아니면서, 체육복이 없는 학생인 경우
    if (i !== 0 && student[i] === 0) {
      // 앞 친구가 여벌의 체육복이 있는지 확인한 후 체육복을 분배
      if (student[i - 1] === 2) {
        student[i - 1]--;
        student[i]++;
        // 체육복을 얻었으면 바로 다음 학생으로 건너간다. continue가 없으면 아래 로직을 또 타게 된다.
        continue;
      }
    }
    // 맨 뒷 사람이 아니면서, 체육복이 없는 학생인 경우
    if (i !== student.length - 1 && student[i] === 0) {
      // 뒷 친구가 여벌의 체육복이 있는지 확인한 후 체육복을 분배
      if (student[i + 1] === 2) {
        student[i + 1]--;
        student[i]++;
      }
    }
  }
  return student.filter((item) => item >= 1).length;
};

export default solution;
