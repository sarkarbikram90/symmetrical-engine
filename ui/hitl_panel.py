import streamlit as st
from datetime import datetime
import json

def hitl_panel(actions, metrics):
    st.subheader("✋ Human-in-the-Loop Approval Required")

    st.json({
        "proposed_actions": actions,
        "system_metrics": metrics
    })

    decision = st.radio("Approve these actions? (future models will be trained on your actions)", ("Approve", "Reject"))
    notes = st.text_area("Reviewer notes")

    if st.button("Submit Decision"):
        record = {
            "timestamp": str(datetime.utcnow()),
            "decision": decision,
            "notes": notes,
            "actions": actions,
            "metrics": metrics
        }

        with open("audit/action_log.json", "a") as f:
            f.write(json.dumps(record) + "\n")

        return decision

    return None
