import { solution } from './changeBracket.js';

describe('changeBracket TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = "(()())()";
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "(()())()"', (done) => {
    const element1 = "(()())()";
    expect(solution(element1)).toEqual("(()())()");
    done();
  });

  test('should return "()"', (done) => {
    const element1 = ")(";
    expect(solution(element1)).toEqual('()');
    done();
  });
  
});