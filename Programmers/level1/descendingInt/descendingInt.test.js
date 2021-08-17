import { solution } from './descendingInt.js';

describe('descendingInt TEST', () => {
    test('should return type of result "number"', (done) => {
      expect(typeof solution(118372)).toEqual('number');
      done();
    });
  
    test('should return 873211', (done) => {
      expect(solution(118372)).toEqual(873211);
      done();
    });
  
    test('should return 11111', (done) => {
      expect(solution(11111)).toEqual(11111);
      done();
    });

    test('should return 54321', (done) => {
        expect(solution(51243)).toEqual(54321);
        done();
      });
  });