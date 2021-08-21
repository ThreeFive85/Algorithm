import { solution } from './findKim.js';

describe('findKim TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = ['park', 'kim']
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "김서방은 1에 있다"', (done) => {
    const element1 = ['Park', 'Kim']
    expect(solution(element1)).toEqual('김서방은 1에 있다');
    done();
  });

  test('should return "김서방은 0에 있다"', (done) => {
    const element1 = ['Kim', 'Park']
    expect(solution(element1)).toEqual('김서방은 0에 있다');
    done();
  });

  test('should return "김서방은 존재하지 않는다"', (done) => {
    const element1 = ['Park', 'Lee']
    expect(solution(element1)).toEqual('김서방은 존재하지 않는다');
    done();
  });
});