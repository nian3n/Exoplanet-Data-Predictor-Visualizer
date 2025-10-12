#                                             Model Evaluation.py
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
'''
This "Model Evaluation" is more a recopliation of what was already done, at least this implementation doesn't work with 
new data

Can be implemented to just predict whatever other Koi Dataset or work from here
'''
                         
csv_path = "https://raw.githubusercontent.com/MatiasPF1/KOI-Dataset/main/NasaDataset.csv" # As Said before , we can change this or even erase
# Resolve model path relative to this script so it works regardless of current working directory
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'model.pkl')

# --- Columns to drop 
drop_cols = [
    'kepid', 'kepoi_name', 'kepler_name', 'koi_pdisposition', 'koi_score',
    'koi_teq_err1', 'koi_teq_err2', 'koi_tce_delivname', 'ra', 'koi_time0bk', 'dec',
    'koi_period_err1', 'koi_period_err2', 'koi_duration_err1', 'koi_duration_err2',
    'koi_depth_err1', 'koi_depth_err2', 'koi_prad_err1', 'koi_prad_err2',
    'koi_insol_err1', 'koi_insol_err2', 'koi_impact_err1', 'koi_impact_err2',
    'koi_steff_err1', 'koi_steff_err2', 'koi_slogg_err1', 'koi_slogg_err2',
    'koi_srad_err1', 'koi_srad_err2'
]


# --- Load data and drop unwanted columns
df = pd.read_csv(csv_path)
df = df.drop(columns=drop_cols)

# --- Filter and map labels
df = df[df["koi_disposition"] != "FALSE POSITIVE"].copy()
label_map = {'CONFIRMED': 0, 'CANDIDATE': 1}

# Use replace then ensure dtype is numeric to avoid future downcasting warnings
df['koi_disposition'] = df['koi_disposition'].replace(label_map).astype(int)
y = df['koi_disposition'].values

# --- Select features
feature_cols = [c for c in df.columns if c != 'koi_disposition']
X = df[feature_cols].values

# --- Load model and predict ---
model = joblib.load(model_path)
y_pred = model.predict(X)

# --- Evaluate
y_pred_int = y_pred.astype(int)
acc = accuracy_score(y, y_pred_int)
print("Accuracy:", acc)
print("Confusion matrix:\n", confusion_matrix(y, y_pred_int))
print("Classification report:\n", classification_report(y, y_pred_int))