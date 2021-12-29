import { solution } from './jadenCase.js';

describe('jadenCase TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = "3people unFollowed me";	
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "3people Unfollowed Me"', (done) => {
    const element1 = "3people unfollowed me";
    expect(solution(element1)).toEqual("3people Unfollowed Me");
    done();
  });

  test('should return "for the last week"', (done) => {
    const element1 = "for the last week";
    expect(solution(element1)).toEqual("For The Last Week");
    done();
  });
  
});