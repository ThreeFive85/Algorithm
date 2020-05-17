/**
 * A prime number is a whole number that has no other divisors other than
 * itself and 1. Write a function that accepts a number and returns true if it's
 * a prime number, false if it's not.
 * 참고 레퍼런스 (왜 소수의 제곱근을 사용하여 소수를 확인하는지)
 * https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-prime-number-to-determine-if-it-is-pr
 */

const primeTester = (n) => {
  if (typeof n !== 'number' || n < 1 || n % 1 !== 0) {
    return false;
  }
  if (n === 1) {
    return false;
  }

  let num = Math.sqrt(n);

  for (let i = 2; i <= num; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};

const primeSieve = (start, end) => {
  let result = [];

  for (let i = start; i <= end; i++) {
    if (primeTester(i) === true) {
      result.push(i);
    }
  }
  return result;
};

module.exports = {
  primeTester: primeTester,
  primeSieve: primeSieve,
};
