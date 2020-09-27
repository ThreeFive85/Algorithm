import solution from './craneDollMachine';

describe('craneDollMachine TEST', () => {
  test('should be return type number of solution()', (done) => {
    const board = [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ];
    const moves = [1, 5, 3, 5, 1, 2, 1, 4];
    const result = solution(board, moves);

    expect(typeof result).toEqual('number');
    done();
  });

  test('should be return 4 number of solution(board, moves)', (done) => {
    const board = [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ];
    const moves = [1, 5, 3, 5, 1, 2, 1, 4];
    const result = solution(board, moves);

    expect(result).toEqual(4);
    done();
  });
});
