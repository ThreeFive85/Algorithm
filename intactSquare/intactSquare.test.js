import solution from './intactSquare';

describe('intactSquare TEST', () => {
  test('should be return type number of solution(w, h)', (done) => {
    const result = solution(3, 3);
    expect(typeof result).toEqual('number');
    done();
  });

  test('should be return 6 of solution(3,3)', (done) => {
    const result = solution(3, 3);
    expect(result).toEqual(6);
    done();
  });

  test('should be return 6 of solution(8,12)', (done) => {
    const result = solution(8, 12);
    expect(result).toEqual(80);
    done();
  });
});
