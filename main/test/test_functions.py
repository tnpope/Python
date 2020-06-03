import unittest
from main import camper_age_input


class MyTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        self.assertEqual(60, camper_age_input.convert_to_months(5))


if __name__ == '__main__':
    unittest.main()
