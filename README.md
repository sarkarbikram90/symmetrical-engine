# 🛠️ Autonomous System Diagnostics with Auto-Healing & Human-in-the-Loop (HITL)

A production-inspired demo showcasing **governed autonomy** in system operations — where **safe issues heal themselves**, and **risky actions require human approval**.

This project demonstrates how **machine learning + policy + human judgment** can work together to build **trustworthy self-healing systems**.

---

## 🚀 What This Project Does

This system continuously evaluates **system health signals** such as:

- Disk usage
- Memory usage
- CPU utilization
- DNS latency
- Firewall change requests

Using a trained ML model, it classifies the **operational risk level** and decides one of three outcomes:

| Decision | Meaning |
|--------|--------|
| ✅ **NO_ACTION** | System is healthy |
| ⚡ **AUTO_HEAL** | Safe remediation executed automatically |
| ✋ **HITL_REQUIRED** | Risky action requires human approval |

The result is a **clear, explainable, and auditable remediation workflow**.

---

## 🎯 Why This Problem?

Many “self-healing” systems fail because they:
- Automate **everything** (high risk)
- Or rely entirely on humans (slow, unscalable)

This project demonstrates a **balanced approach**:

> **Autonomy where safe.  
> Human control where risky.**

This mirrors real-world operational decision-making in:
- Infrastructure platforms
- SRE / DevOps systems
- Security operations
- AI governance systems

---

## 🧠 Core Design Principles

- **ML for risk classification**, not blind automation
- **Deterministic decisions** (no randomness in outcomes)
- **Human-in-the-Loop for high-blast-radius actions**
- **Clear separation of concerns**
- **Auditability by design**

---

## 🧩 High-Level Workflow
## 🔁 System Workflow

```mermaid
flowchart TD
    A[System Metrics<br/>(Synthetic / Live)] --> B[Feature Builder]
    B --> C[ML Severity Classifier]
    C --> D[Decision Engine]

    D -->|AUTO_HEAL<br/>(Safe)| E[Auto Remediation]
    D -->|HITL_REQUIRED<br/>(Risky)| F[Human Approval UI]

    E --> G[Action Taken]
    F --> H[Approve / Reject]

    G --> I[Audit Log<br/>(Governance)]
    H --> I
```



## 🤖 The ML Model (Simple, Explainable, Purposeful)

### Model Objective
Classify **operational severity**, not predict complex time-series.

### Input Features
- `disk_usage (%)`
- `memory_usage (%)`
- `cpu_usage (%)`
- `dns_latency (ms)`
- `firewall_change_requested (0/1)`

### Output Classes
| Class | Meaning |
|-----|--------|
| `0` | NO_ACTION |
| `1` | AUTO_HEAL |
| `2` | HITL_REQUIRED |

The model is trained **locally** using MLflow and exported as an approved artifact.

---

## 🔁 Auto-Healing vs HITL (By Design)

### ✅ Auto-Healing (Safe)
Actions that are:
- Reversible
- Low blast radius
- Operationally safe

Examples:
- Disk cleanup
- Memory cleanup
- Restarting a high-CPU service

### ✋ Human-in-the-Loop (Risky)
Actions that are:
- Security-sensitive
- Network-impacting
- Potentially disruptive

Examples:
- DNS configuration changes
- Firewall port modifications

This distinction is intentional and realistic.

---

## 🧑‍⚖️ Human-in-the-Loop Experience

When HITL is required, the UI shows:
- Current system metrics
- Proposed actions
- Approval / rejection controls
- Notes for context

Every human decision is **logged for auditability**.

---

## 📊 Streamlit UI Features

- 🔄 **Refresh button** to pull live metrics
- 📊 Live system diagnostics
- 🧭 Clear decision banner
- ⚡ Auto-healing status
- ✋ HITL approval workflow
- 🧾 Audit trail (JSON-based)

Designed to feel like a **real operations console**, not a toy demo.


## 🧪 How to Run Locally

### 1️⃣ Train the model (once)
```bash
python -m model.train_severity_model

```
## Run the UI

```bash
streamlit run app.py
```




