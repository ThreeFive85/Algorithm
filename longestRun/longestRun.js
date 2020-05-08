/**
 * Write a function that, given a string, Finds the longest run of identical
 * characters and returns an array containing the start and end indices of
 * that run. If there are two runs of equal length, return the first one.
 * For example:
 *
 *   longestRun("abbbcc") // [1, 3]
 *   longestRun("aabbc")  // [0, 1]
 *   longestRun("abcd")   // [0, 0]
 *
 * Try your function with long, random strings to make sure it handles large
 * inputs well.
 */

const longestRun = (string) => {
  let res = [0, 0];
  let cur = [0, 0];

  for (let i = 0; i < string.length; i++) {
    if (string[i - 1] === string[i]) {
      cur[1] = i;
      if (cur[1] - cur[0] > res[1] - res[0]) {
        res = cur;
      }
    } else {
      cur = [i, i];
    }
  }
  return res;
};

export default longestRun;
