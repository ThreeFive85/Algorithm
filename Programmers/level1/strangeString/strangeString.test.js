import { solution } from './strangeString.js';

describe('strangeString TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = "try hello world"
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "TrY HeLlO WoRlD"', (done) => {
    const element1 = "try hello world"
    expect(solution(element1)).toEqual("TrY HeLlO WoRlD");
    done();
  });

  test('should return " HeLlO EvErYoNe "', (done) => {
    const element1 = " Hello eVeryone "
    expect(solution(element1)).toEqual(" HeLlO EvErYoNe ");
    done();
  });

  test('should return "AaAaAaAaAaA A A A A AaAaA AaA "', (done) => {
    const element1 = "AAAAAAAAAAA A A A A AAAAA AAA "
    expect(solution(element1)).toEqual("AaAaAaAaAaA A A A A AaAaA AaA ");
    done();
  });
});