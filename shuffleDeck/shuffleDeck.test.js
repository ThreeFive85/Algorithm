import shuffleDeck from './shuffleDeck';

const orderedDeck = () => {
  let suits = ['♥', '♣', '♠', '♦'];
  let values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'];
  let deck = [];

  suits.forEach((suit) => {
    values.forEach((value) => {
      deck.push(suit + value);
    });
  });
  return deck;
};

describe('shuffleDeck TEST', () => {
  test('should not return the deck in input order', (doen) => {
    const input = orderedDeck();
    const control = orderedDeck();
    expect(shuffleDeck(input)).not.toBe(control);
    doen();
  });

  test('should not return the deck in the same order twice', (doen) => {
    const input1 = orderedDeck();
    const input2 = orderedDeck();
    expect(shuffleDeck(input1)).not.toBe(shuffleDeck(input2));
    doen();
  });
});
