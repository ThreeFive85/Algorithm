import solution from './124world';

describe('solution TEST', () => {
  test('should be return type String of solution(n)', (done) => {
    expect(typeof solution(1)).toEqual('string');
    done();
  });

  test("should be return '1' of solution(1)", (done) => {
    expect(solution(1)).toEqual('1');
    done();
  });

  test("should be return '2' of solution(2)", (done) => {
    expect(solution(2)).toEqual('2');
    done();
  });

  test("should be return '3' of solution(4)", (done) => {
    expect(solution(3)).toEqual('4');
    done();
  });

  test("should be return '11' of solution(4)", (done) => {
    expect(solution(4)).toEqual('11');
    done();
  });

  test("should be return '41' of solution(10)", (done) => {
    expect(solution(10)).toEqual('41');
    done();
  });
});
