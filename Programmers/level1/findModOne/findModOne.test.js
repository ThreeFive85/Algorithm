import { solution } from './findModOne.js';

describe('findModOne TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 10;
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 3', (done) => {
    const element1 = 10;
    expect(solution(element1)).toEqual(3);
    done();
  });

  test('should return 11', (done) => {
    const element1 = 12;
    expect(solution(element1)).toEqual(11);
    done();
  });
  
});