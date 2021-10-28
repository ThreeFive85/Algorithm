import { solution } from './addExistNumber.js';

describe('addExistNumber TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [1,2,3,4,6,7,8,0];
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 14', (done) => {
    const element1 = [1,2,3,4,6,7,8,0];
    expect(solution(element1)).toEqual(14);
    done();
  });

  test('should return 6', (done) => {
    const element1 = [5,8,4,0,6,7,9];
    expect(solution(element1)).toEqual(6);
    done();
  });

});