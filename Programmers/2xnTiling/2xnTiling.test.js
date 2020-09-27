import solution from './2xnTiling';

describe('2xnTiling TEST', () => {
  test('should be return type number of solution(n)', (done) => {
    const result = solution(4);
    expect(typeof result).toEqual('number');
    done();
  });

  test('should be return 5 of solution(4)', (done) => {
    const result = solution(4);
    expect(result).toEqual(5);
    done();
  });
});
