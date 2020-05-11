import mergeSort from './mergeSort';

describe('mergeSort TEST', () => {
  test('should return an array with a single number', (done) => {
    const result = mergeSort([1]);
    expect(result).toEqual([1]);
    done();
  });

  test('should sort a short array of integers', (done) => {
    const result = mergeSort([8, 7, 3, 6, 9, 2, 4, 5, 1]);
    expect(result).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    done();
  });
});
