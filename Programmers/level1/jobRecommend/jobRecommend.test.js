import { solution } from './jobRecommend.js';

describe('jobRecommend TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
                        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                        "GAME C++ C# JAVASCRIPT C JAVA"];
    const element2 = ["PYTHON", "C++", "SQL"];
    const element3 = [7,5,5]
    expect(typeof solution(element1, element2, element3)).toEqual('string');
    done();
  });

  test('should return HARDWARE', (done) => {
    const element1 = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
                        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                        "GAME C++ C# JAVASCRIPT C JAVA"];
    const element2 = ["PYTHON", "C++", "SQL"];
    const element3 = [7,5,5];
    expect(solution(element1, element2, element3)).toEqual("HARDWARE");
    done();
  });

  test('should return PORTAL', (done) => {
    const element1 = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
                        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                        "GAME C++ C# JAVASCRIPT C JAVA"];
    const element2 = ["JAVA", "JAVASCRIPT"];
    const element3 = [7,5];
    expect(solution(element1, element2, element3)).toEqual("PORTAL");
    done();
  });
  
});
