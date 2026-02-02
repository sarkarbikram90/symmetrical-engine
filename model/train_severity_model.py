import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from data.generate_system_metrics import generate_system_metrics

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


X = []
y = []

# Generate synthetic training data
for _ in range(500):
    row = generate_system_metrics().iloc[0]

    severity = 0  # NO_ACTION

    if row["disk_usage"] > 85 or row["memory_usage"] > 85:
        severity = 1  # AUTO_HEAL

    if row["dns_latency"] > 250 or row["firewall_change"] == 1:
        severity = 2  # HITL

    X.append(row.values)
    y.append(severity)


X = np.array(X)
y = np.array(y)

mlflow.set_experiment("autonomous-remediation-hitl")

with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=50)
    model.fit(X, y)

    accuracy = model.score(X, y)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

    joblib.dump(model, "model/severity_model.pkl")
    print(f"Model trained with accuracy: {accuracy}")