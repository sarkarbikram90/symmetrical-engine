

import pandas as pd
import numpy as np

def generate_system_metrics():
    return pd.DataFrame([{
        "disk_usage": np.random.randint(40, 95),          # %
        "memory_usage": np.random.randint(30, 95),        # %
        "cpu_usage": np.random.randint(20, 95),           # %
        "dns_latency": np.random.randint(10, 400),        # ms
        "firewall_change": np.random.choice([0, 1], p=[0.9, 0.1])
    }])
