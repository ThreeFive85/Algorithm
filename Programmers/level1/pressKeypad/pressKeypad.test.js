import { solution } from './pressKeypad.js';

describe('pressKeypad TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
    const element2 = 'right';
    expect(typeof solution(element1, element2)).toEqual('string');
    done();
  });

  test('should return "LRLLLRLLRRL"', (done) => {
    const element1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
    const element2 = 'right';
    expect(solution(element1, element2)).toEqual("LRLLLRLLRRL");
    done();
  });

  test('should return "LRLLRRLLLRR"', (done) => {
    const element1 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2];	
    const element2 = 'left';
    expect(solution(element1, element2)).toEqual("LRLLRRLLLRR");
    done();
  });

  test('should return "LLRLLRLLRL"', (done) => {
    const element1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];	
    const element2 = 'right';
    expect(solution(element1, element2)).toEqual("LLRLLRLLRL");
    done();
  });
  
});
