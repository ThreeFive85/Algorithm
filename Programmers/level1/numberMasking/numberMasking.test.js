import { solution } from './numberMasking.js';

describe('numberMasking TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = '01033334444';
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "*******4444"', (done) => {
    const element1 = '01033334444';
    expect(solution(element1)).toEqual('*******4444');
    done();
  });

  test('should return "*****8888"', (done) => {
    const element1 = '027778888';
    expect(solution(element1)).toEqual('*****8888');
    done();
  });

  test('should return "*****1234"', (done) => {
    const element1 = '021231234';
    expect(solution(element1)).toEqual('*****1234');
    done();
  });
});