import { solution } from './recommendNewID.js';

describe('recommendNewID TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = "...!@BaT#*..y.abcdefghijklm";
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "bat.y.abcdefghi"', (done) => {
    const element1 = "...!@BaT#*..y.abcdefghijklm";
    expect(solution(element1)).toEqual("bat.y.abcdefghi");
    done();
  });

  test('should return "z--"', (done) => {
    const element1 = "z-+.^.";
    expect(solution(element1)).toEqual("z--");
    done();
  });

  test('should return "aaa"', (done) => {
    const element1 = "=.=";
    expect(solution(element1)).toEqual("aaa");
    done();
  });
});