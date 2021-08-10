import { solution } from './absPlus.js';

describe('absPlus TEST', () => {
    test('should return type of result "number"', (done) => {
      const element1 = [4,7,12]
      const element2 = [true,false,true]
      expect(typeof solution(element1, element2)).toEqual('number');
      done();
    });
  
    test('should return 9', (done) => {
        const element1 = [4,7,12]
        const element2 = [true,false,true]
      expect(solution(element1, element2)).toEqual(9);
      done();
    });
  
    test('should return 0', (done) => {
      const element1 = [1,2,3]
      const element2 = [false,false,true]
      expect(solution(element1, element2)).toEqual(0);
      done();
    });
  });
  