import longestRun from './longestRun';

describe('longestRun TEST', () => {
  test('should return an array with only two elements', (done) => {
    expect(longestRun('abc').length).toEqual(2);
    expect(longestRun('aabbc').length).toEqual(2);
    done();
  });

  test('should return an array with the `start` and `end` index', (done) => {
    expect(longestRun('abbbcc')).toEqual([1, 3]);
    expect(longestRun('aabbc')).toEqual([0, 1]);
    expect(longestRun('abcd')).toEqual([0, 0]);
    done();
  });

  test('should handle the edge-case of an empty string', (done) => {
    expect(longestRun('')).toEqual([0, 0]);
    done();
  });
});
