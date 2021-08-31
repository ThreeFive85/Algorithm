import { solution } from './oddEven.js';

describe('oddEven TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = 4
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "Even"', (done) => {
    const element1 = 4
    expect(solution(element1)).toEqual('Even');
    done();
  });

  test('should return "Odd"', (done) => {
    const element1 = 3
    expect(solution(element1)).toEqual('Odd');
    done();
  });

  test('should return "Even"', (done) => {
    const element1 = 2
    expect(solution(element1)).toEqual('Even');
    done();
  });
});