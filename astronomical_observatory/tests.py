from django.test import TestCase
from .sources.matrix_helper import MatrixHelper

# Create your tests here.
class MatrixHelperTestCase(TestCase):

    def test_animals_can_speak(self):
        
        matrix = MatrixHelper.get_observed_object(3, 3, '000011001')
        
        self.assertEqual(matrix['width'], 2)
        self.assertEqual(matrix['height'], 2)
        self.assertEqual(matrix['string'], '1101')