import largestProductOfThree from './largestProductOfThree';

describe('largestProductOfThree TEST', () => {
  test('should handle three positive numbers', (done) => {
    expect(largestProductOfThree([0, 2, 3])).toEqual(0);
    expect(largestProductOfThree([2, 3, 5])).toEqual(30);
    expect(largestProductOfThree([7, 5, 3])).toEqual(105);
    expect(largestProductOfThree([7, 5, 7])).toEqual(245);
    done();
  });

  test('should handle more than three positive numbers', (done) => {
    expect(largestProductOfThree([2, 5, 3, 7])).toEqual(105);
    expect(largestProductOfThree([11, 7, 5, 3, 2])).toEqual(385);
    expect(largestProductOfThree([2, 13, 7, 3, 5, 11])).toEqual(1001);
    expect(largestProductOfThree([2, 11, 13, 7, 13, 3, 11, 5])).toEqual(1859);
    done();
  });

  test('should handle all negative numbers', (done) => {
    expect(largestProductOfThree([-5, -4, -3, -2, -1])).toEqual(-6);
    done();
  });
});
