import { solution } from './rotateParen.js';

describe('rotateParen TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = "[](){}";
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 3', (done) => {
    const element1 = "[](){}";
    expect(solution(element1)).toEqual(3);
    done();
  });

  test('should return 2', (done) => {
    const element1 = "}]()[{";
    expect(solution(element1)).toEqual(2);
    done();
  });

  test('should return 0', (done) => {
    const element1 = "[)(]";
    expect(solution(element1)).toEqual(0);
    done();
  });

  test('should return 0', (done) => {
    const element1 = "}}}";
    expect(solution(element1)).toEqual(0);
    done();
  });
});