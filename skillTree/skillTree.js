/**
 * 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/49993
 */

const solution = (skill, skill_trees) => {
  let count = 0;
  let skillArr = skill.split('');

  for (let i = 0; i < skill_trees.length; i++) {
    let treeStr = skill_trees[i]
      .split('')
      .filter((element) => skillArr.includes(element))
      .join('');
    if (treeStr === skill.substring(0, treeStr.length)) {
      count++;
    }
  }
  return count;
};

export default solution;
