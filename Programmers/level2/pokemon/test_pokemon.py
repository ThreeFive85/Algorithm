import unittest
import pokemon


class TestPokemon(unittest.TestCase):

    def test_pokemon1(self):
        argument = [3, 1, 2, 3]
        result = pokemon.solution(argument)
        self.assertEqual(result, 2)

    def test_pokemon2(self):
        argument = [3, 3, 3, 2, 2, 4]
        result = pokemon.solution(argument)
        self.assertEqual(result, 3)

    def test_pokemon3(self):
        argument = [3, 3, 3, 2, 2, 2]
        result = pokemon.solution(argument)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
