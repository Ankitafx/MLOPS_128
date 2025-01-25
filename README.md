# MLOps Foundations Project

This project demonstrates the basics of MLOps by creating a simple machine learning project with a CI/CD pipeline. The project uses the Iris dataset to train a Logistic Regression model.

## Project Structure

```
mlops-foundations/
├── train.py         # Script to train and save the model
├── test.py          # Unit tests for the model and dataset
├── requirements.txt # Dependencies
├── .github/workflows/
│   └── ci-cd.yml    # GitHub Actions workflow for CI/CD
└── README.md        # Project documentation
```

## Steps to Run

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd mlops-foundations
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:
   ```bash
   python train.py
   ```

4. Run tests:
   ```bash
   pytest test.py
   ```

## CI/CD Pipeline

The GitHub Actions pipeline includes the following stages:
1. **Install dependencies**: Installs required Python packages.
2. **Run tests**: Executes unit tests to validate the model and dataset.

## Deliverables

- **Model file**: `model.pkl`
- **Logs**: Outputs from training and testing.
- **GitHub Actions pipeline**: Automated CI/CD pipeline for linting and testing.
