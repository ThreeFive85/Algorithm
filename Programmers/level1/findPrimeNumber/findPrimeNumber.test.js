const solution = (str) => {
  let answer = 0;
  let n = str.split('');
  let nums = new Set();

  permutation(n, '');

  function permutation(a, s) {
    if (s.length > 0) {
      if (nums.has(Number(s)) === false) {
        nums.add(Number(s));
        if (primeTest(Number(s))) {
          answer++;
        }
      }
    }
    if (a.length > 0) {
      for (let i = 0; i < a.length; i++) {
        let t = a.slice(0);
        t.splice(i, 1);
        permutation(t, s + a[i]);
      }
    }
  }

  function primeTest(n) {
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
  }
  return answer;
};

describe('findPrimeNumber TEST', () => {
  test('shoule be return type number of solution()', (done) => {
    const result = solution('17');
    expect(typeof result).toEqual('number');
    done();
  });

  test("shoule be return 3 of solution('17')", (done) => {
    const result = solution('17');
    expect(result).toEqual(3);
    done();
  });

  test("shoule be return 2 of solution('011')", (done) => {
    const result = solution('011');
    expect(result).toEqual(2);
    done();
  });
});
