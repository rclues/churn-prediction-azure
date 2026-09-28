# Customer Churn Prediction — Deployed on Azure ML

An end-to-end machine learning project that predicts customer churn, deployed as a live REST API on Azure, with an interactive frontend and automated retraining via CI/CD.

## Problem

Customer churn (customers leaving a service) directly impacts revenue. This project trains a model to predict which customers are likely to churn, so businesses can intervene proactively.

> **Note:** This project was fully built, deployed, and tested live on Azure ML — see demo screenshots below. The Azure endpoint is currently paused as the free student credits have been used; the code, model, and CI/CD pipeline remain fully functional and can be redeployed.


## Architecture

```
Data (CSV) -> Training (scikit-learn) -> Azure ML Model Registry
    -> Azure ML Managed Online Endpoint (REST API)
    -> Streamlit Frontend (user-facing UI)

GitHub Actions (CI/CD) -> auto-retrains model on data/code changes
```

## Tech Stack

- **ML**: Python, scikit-learn, pandas, joblib
- **Cloud**: Azure Machine Learning (Managed Online Endpoints, Model Registry, Custom Environments)
- **Frontend**: Streamlit
- **CI/CD**: GitHub Actions
- **Version Control**: Git/GitHub

## Model

- **Algorithm**: Logistic Regression
- **Dataset**: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (7,043 customers)
- **Accuracy**: 78.7%
- **Features**: 30 encoded features (contract type, tenure, charges, services, etc.)

## What This Project Demonstrates

- Data cleaning and preprocessing (handling malformed data, encoding categoricals)
- Model training and evaluation with proper train/test methodology
- Cloud deployment as a live, callable REST API
- Secure secrets management (environment variables, never hardcoded)
- Automated CI/CD pipeline for model retraining
- Interactive frontend for non-technical users

## Project Structure

```
churn-prediction-azure/
    data/                   Training dataset
    model_package/          Bundled model + scaler for deployment
    train_model.ipynb       Data prep, training, evaluation
    score.py                Azure ML scoring script (inference logic)
    app.py                  Streamlit frontend
    .github/workflows/      CI/CD pipeline (auto-retraining)
    requirements.txt        Custom environment dependencies
```

## Running Locally

```bash
# Clone the repo
git clone https://github.com/rclues/churn-prediction-azure.git
cd churn-prediction-azure

# Set up environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run the frontend (requires .env with Azure endpoint credentials)
streamlit run app.py
```

## CI/CD

Pushing changes to `data/` or `train_model.ipynb` automatically triggers GitHub Actions to retrain the model and commit the updated model files back to the repository.

## Future Improvements

- Extend CI/CD to auto-redeploy retrained models to the live Azure endpoint
- Add Application Insights monitoring for request/error tracking
- Experiment with additional models (XGBoost, Random Forest) for comparison