import balancedParens from './balancedParens';

describe('balanceParnes TEST', () => {
  test('should return a boolean', (done) => {
    const result = balancedParens('()');
    expect(typeof result).toBe('boolean');
    done();
  });
});

describe('step 1', () => {
  test('should return true for ()', (done) => {
    const result = balancedParens('()');
    expect(result).toEqual(true);
    done();
  });

  test('should return false for (', (done) => {
    const result = balancedParens('(');
    expect(result).toEqual(false);
    done();
  });

  test('should return false for )', (done) => {
    const result = balancedParens(')');
    expect(result).toEqual(false);
    done();
  });

  test('should return false for )(', (done) => {
    const result = balancedParens(')(');
    expect(result).toEqual(false);
    done();
  });

  test('should return true for (())', (done) => {
    const result = balancedParens('(())');
    expect(result).toEqual(true);
    done();
  });

  test('should return false for ))))))))))((((((((((', (done) => {
    const result = balancedParens('))))))))))((((((((((');
    expect(result).toEqual(false);
    done();
  });

  test('should return false for (((((((((())))))))))', (done) => {
    const result = balancedParens('(((((((((())))))))))');
    expect(result).toEqual(true);
    done();
  });

  test('should return false for ())()(()', (done) => {
    const result = balancedParens('())()(()');
    expect(result).toEqual(false);
    done();
  });

  test('should return false for (())()(())', (done) => {
    const result = balancedParens('(())()(())');
    expect(result).toEqual(true);
    done();
  });
});

describe('step 2', () => {
  test('should return false for {', (done) => {
    const result = balancedParens('{');
    expect(result).toEqual(false);
    done();
  });

  test('should return false for }', (done) => {
    const result = balancedParens('}');
    expect(result).toEqual(false);
    done();
  });

  test('should return true for {}', (done) => {
    const result = balancedParens('{}');
    expect(result).toEqual(true);
    done();
  });

  test('should return false for [', (done) => {
    const result = balancedParens('[');
    expect(result).toEqual(false);
    done();
  });

  test('should return false for ]', (done) => {
    const result = balancedParens(']');
    expect(result).toEqual(false);
    done();
  });

  test('should return true for []', (done) => {
    const result = balancedParens('[]');
    expect(result).toEqual(true);
    done();
  });

  test('should return true for [](){}', (done) => {
    const result = balancedParens('[](){}');
    expect(result).toEqual(true);
    done();
  });

  test('should return true for [({})]', (done) => {
    const result = balancedParens('[({})]');
    expect(result).toEqual(true);
    done();
  });

  test('should return false for [(]{)}', (done) => {
    const result = balancedParens('[(]{)}');
    expect(result).toEqual(false);
    done();
  });

  test('should return true for [[[{{{((()))}}}]]]', (done) => {
    const result = balancedParens('[[[{{{((()))}}}]]]');
    expect(result).toEqual(true);
    done();
  });

  test('should return false for []}{()', (done) => {
    const result = balancedParens('[]}{()');
    expect(result).toEqual(false);
    done();
  });
});

describe('step 3', () => {
  test('should return true for this string', (done) => {
    const result = balancedParens(
      'return { name: "Bertrand Russell", birthday: getBirthday({who:self}) };',
    );
    expect(result).toEqual(true);
    done();
  });

  test('should return false for this string', (done) => {
    const result = balancedParens(
      ' var hubble = function() { telescopes.awesome();',
    );
    expect(result).toEqual(false);
    done();
  });

  test('should return true for this string', (done) => {
    const result = balancedParens(' var wow  = { yo: thisIsAwesome() }');
    expect(result).toEqual(true);
    done();
  });

  test('should return true for an empty string', (done) => {
    const result = balancedParens('');
    expect(result).toEqual(true);
    done();
  });
});
