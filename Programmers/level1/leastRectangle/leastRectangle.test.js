import { solution } from './leastRectangle.js';

describe('leastRectangle TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [[60, 50], [30, 70], [60, 30], [80, 40]];
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 4000', (done) => {
    const element1 = [[60, 50], [30, 70], [60, 30], [80, 40]];
    expect(solution(element1)).toEqual(4000);
    done();
  });

  test('should return 120', (done) => {
    const element1 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]];
    expect(solution(element1)).toEqual(120);
    done();
  });
  
});
