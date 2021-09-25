import { solution } from './caesarCipher.js';

describe('caesarCipher TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = "AB"
    const element2 = 1
    expect(typeof solution(element1, element2)).toEqual('string');
    done();
  });

  test('should return "BC"', (done) => {
    const element1 = "AB"
    const element2 = 1
    expect(solution(element1, element2)).toEqual("BC");
    done();
  });

  test('should return "a"', (done) => {
    const element1 = "z"
    const element2 = 1
    expect(solution(element1, element2)).toEqual("a");
    done();
  });
});
