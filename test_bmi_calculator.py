import unittest

from bmi_calculator import BMICalculator

class TestBMICalculator(unittest.TestCase):
    def setUp(self):
        self.bmi_calculator = BMICalculator()

    def test_calculate_bmi(self):
        bmi = self.bmi_calculator.calculate_bmi(1,1)
        self.assertEqual(bmi, 10000.0)

    def test_calculate_bmi_error(self):
        try:
            bmi = self.bmi_calculator.calculate_bmi(1, "XXX")
        except:
            self.assertRaises(ValueError)
        else:
            self.fail("ValueError not raised.")

    def test_overweight_people(self):
        bmi = self.bmi_calculator.get_total_number_of_people_by_category("Overweight")
        self.assertEqual(bmi, 1)

    def test_underweight_people(self):
        bmi = self.bmi_calculator.get_total_number_of_people_by_category("Underweight")
        self.assertEqual(bmi, 0)

    def test_unknown_category_count(self):
        bmi = self.bmi_calculator.get_total_number_of_people_by_category("XXX")
        self.assertEqual(bmi, 0)