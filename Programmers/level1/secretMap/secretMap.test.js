import { solution } from './secretMap.js';

describe('secretMap TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = 5;
    const element2 = [9, 20, 28, 18, 11];
    const element3 = [30, 1, 21, 17, 28];
    expect(typeof solution(element1, element2, element3)).toEqual('object');
    done();
  });

  test('should return ["#####","# # #", "### #", "#  ##", "#####"]', (done) => {
    const element1 = 5;
    const element2 = [9, 20, 28, 18, 11];
    const element3 = [30, 1, 21, 17, 28];
    expect(solution(element1, element2, element3)).toEqual(["#####","# # #", "### #", "#  ##", "#####"]);
    done();
  });

  test('should return ["######", "###  #", "##  ##", " #### ", " #####", "### # "]', (done) => {
    const element1 = 6;
    const element2 = [46, 33, 33 ,22, 31, 50];
    const element3 = [27 ,56, 19, 14, 14, 10];
    expect(solution(element1, element2, element3)).toEqual(["######", "###  #", "##  ##", " #### ", " #####", "### # "]);
    done();
  });

});