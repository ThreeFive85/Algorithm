import theKnumber from './theKnumber';

describe('theKnumber TEST', () => {
  test('should return type of Array', (done) => {
    const result = theKnumber(
      [1, 5, 2, 6, 3, 7, 4],
      [
        [2, 5, 3],
        [4, 4, 1],
        [1, 7, 3],
      ],
    );
    expect(result).toEqual(expect.arrayContaining(result));
    done();
  });

  test('should return right answer', (done) => {
    const result = theKnumber(
      [1, 5, 2, 6, 3, 7, 4],
      [
        [2, 5, 3],
        [4, 4, 1],
        [1, 7, 3],
      ],
    );
    expect(result).toEqual([5, 6, 3]);
    done();
  });
});
