import { solution } from './checkSqrt.js';

describe('checkSqrt TEST', () => {
    test('should return type of result "number"', (done) => {
      expect(typeof solution(121)).toEqual('number');
      done();
    });
  
    test('should return 144', (done) => {
      expect(solution(121)).toEqual(144);
      done();
    });
  
    test('should return -1', (done) => {
      expect(solution(3)).toEqual(-1);
      done();
    });
  });