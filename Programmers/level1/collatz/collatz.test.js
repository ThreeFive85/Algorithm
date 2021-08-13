import { solution } from './collatz.js';

describe('collatz TEST', () => {
    test('should return type of result "number"', (done) => {
      expect(typeof solution(6)).toEqual('number');
      done();
    });
  
    test('should return 8', (done) => {
      expect(solution(6)).toEqual(8);
      done();
    });
  
    test('should return 4', (done) => {
      expect(solution(16)).toEqual(4);
      done();
    });

    test('should return -1', (done) => {
        expect(solution(626331)).toEqual(-1);
        done();
      });
  });