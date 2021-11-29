import { solution } from './functionalDevelopment.js';

describe('functionalDevelopment TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = [93, 30, 55];
    const element2 = [1, 30, 5]; 
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return [2, 1]', (done) => {
    const element1 = [93, 30, 55];
    const element2 = [1, 30, 5]; 
    expect(solution(element1, element2)).toEqual([2, 1]);
    done();
  });

  test('should return [1, 3, 2]', (done) => {
    const element1 = [95, 90, 99, 99, 80, 99];
    const element2 = [1, 1, 1, 1, 1, 1];
    expect(solution(element1, element2)).toEqual([1, 3, 2]);
    done();
  });

});
