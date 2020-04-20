import bubbleSort from './bubbleSort';

describe('bubbleSort TEST', () => {
  test('should sort an array numerically', (done) => {
    const input = [1, 2, 43, 100, 100, 21, 21];
    const expected = [1, 2, 21, 21, 43, 100, 100];
    expect(bubbleSort(input)).toEqual(expected);
    done();
  });

  test('should sort reverse sorted arrays', (done) => {
    expect(bubbleSort([5, 4, 3, 2, 1])).toEqual([1, 2, 3, 4, 5]);
    done();
  });

  test('should handle presorted arrays', (done) => {
    expect(bubbleSort([1, 2, 3, 4, 5])).toEqual([1, 2, 3, 4, 5]);
    done();
  });

  test('should sort arrays with negative numbers', (done) => {
    const input = [20, -10, -10.1, 2, 4, 299];
    const expected = [-10.1, -10, 2, 4, 20, 299];
    expect(bubbleSort(input)).toEqual(expected);
    done();
  });
});
