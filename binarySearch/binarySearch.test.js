import binarySearch from './binarySearch';

describe('binarySearch TEST', () => {
  test('should output return number', (done) => {
    const result = binarySearch([5], 5);
    expect(typeof result).toBe('number');
    done();
  });

  test('should return 0 for 5 in [5]', (done) => {
    const result = binarySearch([5], 5);
    expect(result).toEqual(0);
    done();
  });

  test('should return null for 4 in [5]', (done) => {
    const result = binarySearch([5], 4);
    expect(result).toEqual(null);
    done();
  });

  test('should return 0 for 1 in [1, 2, 3, 4, 5]', (done) => {
    const result = binarySearch([1, 2, 3, 4, 5], 1);
    expect(result).toEqual(0);
    done();
  });

  test('should return 1 for 2 in [1, 2, 3, 4, 5]', (done) => {
    const result = binarySearch([1, 2, 3, 4, 5], 2);
    expect(result).toEqual(1);
    done();
  });

  test('should return 2 for 3 in [1, 2, 3, 4, 5]', (done) => {
    const result = binarySearch([1, 2, 3, 4, 5], 3);
    expect(result).toEqual(2);
    done();
  });

  test('should return 3 for 4 in [1, 2, 3, 4, 5]', (done) => {
    const result = binarySearch([1, 2, 3, 4, 5], 4);
    expect(result).toEqual(3);
    done();
  });

  test('should return 4 for 5 in [1, 2, 3, 4, 5]', (done) => {
    const result = binarySearch([1, 2, 3, 4, 5], 5);
    expect(result).toEqual(4);
    done();
  });

  test('should return 3 for 45 in [1, 22, 33, 45, 53, 62]', (done) => {
    const result = binarySearch([11, 22, 33, 45, 53, 62], 45);
    expect(result).toEqual(3);
    done();
  });
});
