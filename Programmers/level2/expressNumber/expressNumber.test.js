import { solution } from './expressNumber.js';

describe('expressNumber TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 15;
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 4', (done) => {
    const element1 = 15;
    expect(solution(element1)).toEqual(4);
    done();
  });

});