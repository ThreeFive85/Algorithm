import { solution } from './waterMelon.js';

describe('waterMelon TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = 3;
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "수박수', (done) => {
    const element1 = 3;
    expect(solution(element1)).toEqual("수박수");
    done();
  });

  test('should return "수박수박"', (done) => {
    const element1 = 4;
    expect(solution(element1)).toEqual('수박수박');
    done();
  });

});