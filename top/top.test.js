import solution from './top';

describe('top TEST', () => {
  test('should be return [0,0,2,2,4] of solution([6,9,5,7,4])', (done) => {
    const result = solution([6, 9, 5, 7, 4]);
    expect(result).toEqual([0, 0, 2, 2, 4]);
    done();
  });

  test('should be return [0,0,2,0,0,5,6] of solution([1,5,3,6,7,6,5])', (done) => {
    const result = solution([1, 5, 3, 6, 7, 6, 5]);
    expect(result).toEqual([0, 0, 2, 0, 0, 5, 6]);
    done();
  });

  test('should be return [0,0,0,3,3,3,6] of solution([3,9,9,3,5,7,2])', (done) => {
    const result = solution([3, 9, 9, 3, 5, 7, 2]);
    expect(result).toEqual([0, 0, 0, 3, 3, 3, 6]);
    done();
  });
});
