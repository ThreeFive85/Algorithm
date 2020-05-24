import solution from './mockExam';

describe('mockExam TEST', () => {
  test('should return type of array', (done) => {
    const result = solution([1, 2, 3, 4, 5]);
    expect(result).toEqual(expect.arrayContaining(result));
    done();
  });

  test('should return [1]', (done) => {
    const result = solution([1, 2, 3, 4, 5]);
    expect(result).toEqual([1]);
    done();
  });

  test('should return [1,2,3]', (done) => {
    const result = solution([1, 3, 2, 4, 2]);
    expect(result).toEqual([1, 2, 3]);
    done();
  });
});
