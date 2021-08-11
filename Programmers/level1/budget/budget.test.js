import solution from './budget';

describe('budget TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [2,2,3,3]
    const element2 = 10
    expect(typeof solution(element1, element2)).toEqual('number');
    done();
  });

  test('should return 4', (done) => {
    const element1 = [2,2,3,3]
    const element2 = 10
    expect(solution(element1, element2)).toEqual(4);
    done();
  });

  test('should return 3', (done) => {
    const element1 = [1,3,2,5,4]
    const element2 = 9
    expect(solution(element1, element2)).toEqual(3);
    done();
  });
});
