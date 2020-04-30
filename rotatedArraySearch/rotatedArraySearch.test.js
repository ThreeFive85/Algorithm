import rotatedArraySearch from './rotatedArraySearch';

describe('rotatedArraySearch TEST', () => {
  test('should return a number', (done) => {
    expect(typeof rotatedArraySearch([3, 4, 5, 2], 4)).toBe('number');
    done();
  });

  test('should return the index of that item', (done) => {
    expect(rotatedArraySearch([4, 5, 6, 0, 1, 2, 3], 1)).toEqual(4);
    done();
  });

  test('and a value that is not in the array', (done) => {
    expect(rotatedArraySearch([1, 2, 3], 5)).toBe(null);
    done();
  });
});
