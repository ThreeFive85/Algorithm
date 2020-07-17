import solution from './workoutClothes';

describe('workoutClothes TEST', () => {
  test('should be return type number of solution()', (done) => {
    const result = solution(5, [2, 4], [1, 3, 5]);
    expect(typeof result).toEqual('number');
    done();
  });

  test('should be return 5 of solution(5,[2, 4],[1, 3, 5])', (done) => {
    const result = solution(5, [2, 4], [1, 3, 5]);
    expect(result).toEqual(5);
    done();
  });

  test('should be return 4 of solution(5,[2, 4],[3])', (done) => {
    const result = solution(5, [2, 4], [3]);
    expect(result).toEqual(4);
    done();
  });

  test('should be return 2 of solution(3,[3],[1])', (done) => {
    const result = solution(3, [3], [1]);
    expect(result).toEqual(2);
    done();
  });
});
