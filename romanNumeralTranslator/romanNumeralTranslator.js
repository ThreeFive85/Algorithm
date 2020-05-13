/**
 * Given a roman numeral as input, write a function that converts the roman
 * numeral to a number and outputs it.
 *
 * Ex:
 * translateRomanNumeral("LX") // 60
 *
 * When a smaller numeral appears before a larger one, it becomes
 * a subtractive operation. You can assume only one smaller numeral
 * may appear in front of larger one.
 *
 * Ex:
 * translateRomanNumeral("IV") // 4
 *
 * You should return `null` on invalid input.
 */

const DIGIT_VALUES = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

const translateRomanNumeral = (romanNumeral) => {
  let result = 0;
  let currentValue;
  let nextValue;

  if (romanNumeral.length === 1) {
    return DIGIT_VALUES[romanNumeral];
  } else if (romanNumeral === 50) {
    return null;
  }

  for (let i = 0; i < romanNumeral.length; i++) {
    currentValue = DIGIT_VALUES[romanNumeral[i]];
    nextValue = DIGIT_VALUES[romanNumeral[i + 1]];

    if (currentValue < nextValue) {
      result -= currentValue;
    } else {
      result += currentValue;
    }
  }

  return result;
};

export default translateRomanNumeral;
