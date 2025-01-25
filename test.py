#CICD Test
import unittest
import pickle
import numpy as np
from sklearn.datasets import load_iris

class TestModel(unittest.TestCase):

    def test_dataset_shape(self):
        # Load dataset
        iris = load_iris()
        X, y = iris.data, iris.target
        
        # Check shape
        self.assertEqual(X.shape, (150, 4))
        self.assertEqual(y.shape, (150,))

    def test_model_prediction(self):
        # Load model
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)

        # Predict sample
        sample = np.array([[5.1, 3.5, 1.4, 0.2]])
        prediction = model.predict(sample)
        
        # Check prediction type
        self.assertIn(prediction[0], [0, 1, 2])

if __name__ == "__main__":
    unittest.main()
