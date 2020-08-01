import solution from './skillTree';

describe('skillTree TEST', () => {
  test('should be type return number of solution(skill, skill_trees)', (done) => {
    const result = solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']);
    expect(typeof result).toEqual('number');
    done();
  });

  test(`should be return 2 of solution("CBD", 
    ["BACDE", "CBADF", "AECB", "BDA"])`, (done) => {
    const result = solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']);
    expect(result).toEqual(2);
    done();
  });
});
