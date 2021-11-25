import { solution } from './findPrime.js';

describe('findPrime TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = "17";
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 3', (done) => {
    const element1 = "17";
    expect(solution(element1)).toEqual(3);
    done();
  });

  test('should return 2', (done) => {
    const element1 = "011";
    expect(solution(element1)).toEqual(2);
    done();
  });

});