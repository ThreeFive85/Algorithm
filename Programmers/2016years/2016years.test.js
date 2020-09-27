import solution from './2016years';

describe('2016years TEST', () => {
  test('should return type of result "string"', (done) => {
    expect(typeof solution(5, 24)).toEqual('string');
    done();
  });

  test('should return "TUE"', (done) => {
    expect(solution(5, 24)).toEqual('TUE');
    done();
  });

  test('should return "MON"', (done) => {
    expect(solution(2, 8)).toEqual('MON');
    done();
  });

  test('should return "TUE"', (done) => {
    expect(solution(8, 9)).toEqual('TUE');
    done();
  });

  test('should return error message if non-existent date', (done) => {
    expect(solution(13, 35)).toEqual('존재하지 않는 날짜입니다');
    expect(solution(1, 35)).toEqual('존재하지 않는 날짜입니다');
    expect(solution(13, 3)).toEqual('존재하지 않는 날짜입니다');
    done();
  });
});
