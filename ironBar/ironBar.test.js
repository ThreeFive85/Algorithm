import solution from './ironBar';

describe('ironBar TEST', () => {
  test('should be return type number of solution()', (done) => {
    const result = solution('(())');
    expect(typeof result).toEqual('number');
    done();
  });

  test("should be return 2 number of solution('(())')", (done) => {
    const result = solution('(())');
    expect(result).toEqual(2);
    done();
  });

  test("should be return 3 number of solution('(()())')", (done) => {
    const result = solution('(()())');
    expect(result).toEqual(3);
    done();
  });

  test("should be return 17 number of solution('()(((()())(())()))(())')", (done) => {
    const result = solution('()(((()())(())()))(())');
    expect(result).toEqual(17);
    done();
  });
});
