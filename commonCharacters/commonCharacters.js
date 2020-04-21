/**
 * Write a function `f(a, b)` which takes two strings as arguments and returns a
 * string containing the characters found in both strings (without duplication), in the
 * order that they appeared in `a`. Remember to skip spaces and characters you
 * have already encountered!
 *
 * Example: commonCharacters('acexivou', 'aegihobu')
 * Returns: 'aeiou'
 *
 * Extra credit: Extend your function to handle more than two input strings.
 */

const commonCharacters = (...str) => {
  let obj = {};
  let result = '';

  for (let i = 0; i < str.length; i++) {
    for (let j = 0; j < str[i].length; j++) {
      if (obj[str[i][j]] === undefined) {
        obj[str[i][j]] = 0;
      }
      obj[str[i][j]]++;
    }
  }
  for (let z in obj) {
    if (obj[z] === str.length) {
      result += z;
    }
  }
  return result;
};

export default commonCharacters;
