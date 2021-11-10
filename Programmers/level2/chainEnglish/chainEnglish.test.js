import { solution } from './chainEnglish.js';

describe('chainEnglish TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = 3;
    const element2 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"];
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return [3,3]', (done) => {
    const element1 = 3;
    const element2 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"];
    expect(solution(element1, element2)).toEqual([3,3]);
    done();
  });

  test('should return [2,1]', (done) => {
    const element1 = 2;
    const element2 = ["hello", "one", "even", "never", "now", "world", "draw"];
    expect(solution(element1, element2)).toEqual([1,3]);
    done();
  });
  
});