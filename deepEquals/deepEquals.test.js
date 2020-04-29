import deepEquals from './deepEquals';

describe('deepEquals TEST', () => {
  test('should use deep equality', (done) => {
    const a = { foo: 1 };
    const b = { foo: '1' };
    expect(deepEquals(a, b)).toEqual(false);
    done();
  });

  test('should return true for two objects with the same keys and values', (done) => {
    const a = { foo: 'bar' };
    const b = { foo: 'bar' };
    expect(deepEquals(a, b)).toEqual(true);
    done();
  });

  test('should return false for two objects with the same keys and but different values', (done) => {
    const a = { foo: 'bar' };
    const b = { foo: 'pow' };
    expect(deepEquals(a, b)).toEqual(false);
    done();
  });

  test('should return false for two objects with different number of keys', (done) => {
    const a = { foo: 'bar' };
    const b = { foo: 'bar', biz: 'baz' };
    expect(deepEquals(a, b)).toEqual(false);
    done();
  });
  test('should return false for two objects with different number of keys', (done) => {
    const a = { foo: 'bar', biz: 'baz' };
    const b = { foo: 'bar' };
    expect(deepEquals(a, b)).toEqual(false);
    done();
  });
  test('should return true for similar nested object properties', (done) => {
    const a = { foo: 1, b: { c: 3 } };
    const b = { foo: 1, b: { c: 3 } };
    expect(deepEquals(a, b)).toEqual(true);
    done();
  });
  test('should return false for dissimilar nested object properties', (done) => {
    const a = { foo: 1, b: { c: 3 } };
    const b = { foo: 1, b: { c: 'potato' } };
    expect(deepEquals(a, b)).toEqual(false);
    done();
  });
  test('should return false for dissimilar nested object properties', (done) => {
    const a = { foo: 1, b: { c: 'potato' } };
    const b = { foo: 1, b: { c: 3 } };
    expect(deepEquals(a, b)).toEqual(false);
    done();
  });
  test('should return true for similar excessively nested object properties', (done) => {
    const a = { foo: 1, b: { c: { d: { e: 'potato' } } } };
    const b = { foo: 1, b: { c: { d: { e: 'potato' } } } };
    expect(deepEquals(a, b)).toEqual(true);
    done();
  });
  test('should return true for similar excessively nested object properties', (done) => {
    const a = { b: { c: { d: { e: 'potato' } } }, foo: 1 };
    const b = { foo: 1, b: { c: { d: { e: 'potato' } } } };
    expect(deepEquals(a, b)).toEqual(true);
    done();
  });
});
