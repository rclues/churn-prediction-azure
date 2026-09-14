import json
import joblib
import numpy as np
import os

def init():
    global model, scaler
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model_package', 'model.pkl')
    scaler_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model_package', 'scaler.pkl')
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

def run(raw_data):
    data = json.loads(raw_data)['data']
    data_scaled = scaler.transform(np.array(data))
    predictions = model.predict(data_scaled)
    return predictions.tolist()