import { solution } from './immigration.js';

describe('immigration TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 6;
    const element2 = [7, 10];
    expect(typeof solution(element1, element2)).toEqual('number');
    done();
  });

  test('should return 28', (done) => {
    const element1 = 6;
    const element2 = [7, 10];
    expect(solution(element1, element2)).toEqual(28);
    done();
  });

});