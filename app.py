import streamlit as st
import joblib

from data.generate_system_metrics import generate_system_metrics
from decision.decision_engine import decide_action, Decision
from remediation.auto_heal import auto_heal
from remediation.hitl_actions import risky_actions
from ui.hitl_panel import hitl_panel

st.set_page_config(page_title="Autonomous Remediation with HITL", layout="wide")
st.title("🛠️ Autonomous System Diagnostics + Human-in-the-loop")

# Generate metrics
metrics_df = generate_system_metrics()
metrics = metrics_df.iloc[0].to_dict()

st.subheader("📊 Live System Metrics")
st.json(metrics)

# Load ML model
model = joblib.load("model/severity_model.pkl")

prediction = model.predict([list(metrics.values())])[0]
decision = decide_action(prediction)

LABELS = {
    Decision.NO_ACTION: "System Healthy",
    Decision.AUTO_HEAL: "Auto-Healing Triggered",
    Decision.HITL_REQUIRED: "Human Approval Required"
}

st.metric("🧭 Decision", LABELS[decision])

st.divider()

# Action handling
if decision == Decision.AUTO_HEAL:
    actions = auto_heal(metrics)
    st.success("⚡ Auto-Healing Executed")
    st.write(actions)

elif decision == Decision.HITL_REQUIRED:
    actions = risky_actions(metrics)
    result = hitl_panel(actions, metrics)

    if result == "Approve":
        st.success("✅ Human-approved actions executed")
    elif result == "Reject":
        st.error("❌ Actions rejected by human")

else:
    st.success("✅ No action required")
