/*
 * write a function that takes a string of text and returns true if
 * the parentheses are balanced and false otherwise.
 *
 * Example:
 *   balancedParens('(');  // false
 *   balancedParens('()'); // true
 *   balancedParens(')(');  // false
 *   balancedParens('(())');  // true
 *
 * Step 2:
 *   make your solution work for all types of brackets
 *
 * Example:
 *  balancedParens('[](){}'); // true
 *  balancedParens('[({})]');   // true
 *  balancedParens('[(]{)}'); // false
 *
 * Step 3:
 * ignore non-bracket characters
 * balancedParens(' var wow  = { yo: thisIsAwesome() }'); // true
 * balancedParens(' var hubble = function() { telescopes.awesome();'); // false
 *
 *
 */

import binarySearch from '../binarySearch/binarySearch';

const balancedParens = (input) => {
  // (,),{,},[,] 를 담을 배열이 필요
  // 스택 자료구조 사용
  let stackArr = [];
  let strObj = {
    '(': ')',
    '{': '}',
    '[': ']',
  };

  for (let i = 0; i < input.length; i++) {
    if (input[i] === '(' || input[i] === '{' || input[i] === '[') {
      stackArr.push(input[i]);
    } else if (input[i] === ')' || input[i] === '}' || input[i] === ']') {
      let resent = stackArr.pop();
      if (input[i] !== strObj[resent]) {
        // console.log('input[i] : ', input[i]);
        // console.log('strObj[resent] : ', strObj[resent]);
        return false;
      }
    }
  }

  if (stackArr.length !== 0) {
    return false;
  } else {
    return true;
  }
};

export default balancedParens;
