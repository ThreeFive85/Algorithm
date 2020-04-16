/**
 * Given an arbitrary input string, return the first nonrepeated character in
 * the string. For example:
 *
 *   firstNonRepeatedCharacter('ABA'); // => 'B'
 *   firstNonRepeatedCharacter('AACBDB'); // => 'C'
 */

const firstNonRepeatedCharacter = (string) => {
  let obj = {};
  let result = [];

  for (let i = 0; i < string.length; i++) {
    if (obj[string[i]] === undefined) {
      //객체 value값이 없을 때는 초기값 0일 지정해주고
      obj[string[i]] = 0;
    }
    obj[string[i]]++; // 문자가 들어올때마다 하나씩 value값 증가
  } //{A: 2, C: 1, B: 2, D: 1}
  for (let z in obj) {
    if (obj[z] === 1) {
      result.push(z);
    }
  }
  if (result.length === 0) {
    return null;
  } else return result[0];
};

// console.log(firstNonRepeatedCharacter('ABA')); // => 'B'
// console.log(firstNonRepeatedCharacter('AACBDB'));

export default firstNonRepeatedCharacter;
