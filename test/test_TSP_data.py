import unittest
import numpy as np

from main import create_data_model

class TestTspData(unittest.TestCase):
    def test_symmetric_data(self):
        data = create_data_model()
        matrix = np.array(data['distance_matrix'])
        self.assertTrue(np.allclose(matrix, matrix.transpose()))
