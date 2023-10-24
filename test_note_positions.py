import unittest
from note_positions import get_fret, get_frets

class TestNotePositions(unittest.TestCase):

    def test_get_fret_same_note(self):
        self.assertEqual(get_fret("A", "A"), 0)

    def test_get_fret_larger_target(self):
        self.assertEqual(get_fret("C", "A"), 3)

    def test_get_fret_smaller_target(self):
        self.assertEqual(get_fret("A", "C"), 9)

    def test_get_fret_sharp_and_flat(self):
        self.assertEqual(get_fret("G#", "Ab"), 0)

    def test_get_frets_single_string(self):
        frets = get_frets("G", ["G"])
        self.assertEqual(frets, {"G": 0})

    def test_get_frets_multiple_strings(self):
        frets = get_frets("G", ["G", "D", "A", "E"])
        expected_frets = {"G": 0, "D": 5, "A": 10, "E": 3}
        self.assertEqual(frets, expected_frets)

if __name__ == '__main__':
    unittest.main()


