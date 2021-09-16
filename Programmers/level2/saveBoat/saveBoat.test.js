import { solution } from './saveBoat.js';

describe('saveBoat TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [70, 50, 80, 50];
    const element2 = 100;
    expect(typeof solution(element1, element2)).toEqual('number');
    done();
  });

  test('should return 3', (done) => {
    const element1 = [70, 50, 80, 50];
    const element2 = 100;
    expect(solution(element1, element2)).toEqual(3);
    done();
  });

  test('should return 3', (done) => {
    const element1 = [70, 80, 50];
    const element2 = 100;
    expect(solution(element1, element2)).toEqual(3);
    done();
  });

  test('should return 3', (done) => {
    const element1 = [40, 50, 70, 80]
    const element2 = 100;
    expect(solution(element1, element2)).toEqual(3);
    done();
  });
});
