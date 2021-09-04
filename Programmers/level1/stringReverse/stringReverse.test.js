import { solution } from './stringReverse.js';

describe('stringReverse TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = "Zbcdefg"
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "gfedcbZ"', (done) => {
    const element1 = "Zbcdefg"
    expect(solution(element1)).toEqual('gfedcbZ');
    done();
  });

  test('should return "cba"', (done) => {
    const element1 = "abc"
    expect(solution(element1)).toEqual('cba');
    done();
  });

  test('should return "cbaA"', (done) => {
    const element1 = "Aabc"
    expect(solution(element1)).toEqual('cbaA');
    done();
  });
});