import incompletePlayer from './incompletePlayer';

describe('incompletePlayer TEST', () => {
  test('should be return type of incompletePlayer()', (done) => {
    const result = incompletePlayer(['leo', 'kiki', 'eden'], ['kiki', 'eden']);
    expect(typeof result).toEqual('string');
    done();
  });

  test('should be return leo of incompletePlayer([leo, kiki, eden], [kiki, eden])', (done) => {
    const result = incompletePlayer(['leo', 'kiki', 'eden'], ['kiki', 'eden']);
    expect(result).toEqual('leo');
    done();
  });

  test('should be return vinko of incompletePlayer([marina, josipa, nikola, vinko, filipa], [josipa, filipa, marina, nikola])', (done) => {
    const result = incompletePlayer(
      ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
      ['josipa', 'filipa', 'marina', 'nikola'],
    );
    expect(result).toEqual('vinko');
    done();
  });

  test('should be return mislav of incompletePlayer([mislav, stanko, mislav, ana], [stanko, ana, mislav])', (done) => {
    const result = incompletePlayer(
      ['mislav', 'stanko', 'mislav', 'ana'],
      ['stanko', 'ana', 'mislav'],
    );
    expect(result).toEqual('mislav');
    done();
  });
});
