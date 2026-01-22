AEGIS-HUMANITY: Automated AI Audit & Forensic Compliance Suite
1. Overview
AEGIS-HUMANITY is a high-precision forensic auditing framework designed to evaluate financial AI models for gender-based discrimination. Built to align with EU AI Act standards, the suite provides automated bias detection, visual intelligence, and verifiable peer-matching evidence to ensure algorithmic accountability.

2. Architecture & Module Description
The suite is composed of six core functional modules, each handling a critical phase of the audit lifecycle:

A. Data Factory (generate_data.py)
Function: Simulates a high-fidelity dataset of 40,000+ loan applications.

Logic: Incorporates synthetic historical bias to stress-test the audit engine’s detection capabilities.

Standards: Adheres to Ireland/EU financial demographic distributions.

B. Visual Intelligence Suite (visualize_bias.py)
Function: Generates multi-dimensional graphical reports.

Key Outputs: * global_bias.png: Overall approval disparity.

fairness_test.png: Parity metrics across protected attributes.

regional_bias.png: Geographical bias heatmaps.

C. Advanced Model Audit (XAI) (advanced_audit.py)
Function: Conducts Explainable AI (XAI) analysis.

Logic: Uses feature-importance weighting to determine if "Gender" is illegally influencing model decisions over financial merit (Credit Score/Income).

D. Legal Compliance Engine (legal_compliance_audit.py)
Function: Translates technical failures into legal verdicts.

Regulatory Alignment: Maps audit findings directly to Articles 9, 10, and 13 of the EU AI Act.

Encoding: Uses UTF-8 to ensure character integrity for professional PDF/Text reporting.

E. Technical Audit Logging (final_audit_tool.py)
Function: Records low-level statistical metrics.

Metrics: Calculates Disparate Impact Ratio (DIR) and Statistical Parity Difference to provide a "Risk Score" for the model.

F. Factual Forensic Engine (final_forensic_audit.py)
Function: The primary evidence-generation module.

Mechanism: Performs Zero-Trust Peer Matching. It cross-references the database to find a specific "Approved Male" for every "Rejected Qualified Female."

Integrity: Every reported case is 100% traceable to a unique record in the master CSV.

3. Forensic Methodology: "The Peer-Contrast Logic"
Unlike traditional auditors that rely on abstract percentages, AEGIS-HUMANITY utilizes Direct Evidence Extraction:

Identify Victim: Filter for Females with high Credit Scores (700+) who were Rejected.

Scan for Peer: Search the database for Males with equal or lower Credit Scores who were Approved.

Aggregate Scale: Calculate the total volume of lower-merit males approved to prove systemic failure.

Final Verdict: Generate a human-readable forensic trail for legal submission.

4. Installation & Deployment
Bash

# Clone the repository
git clone https://github.com/imran-developer-26/aegis-project.git

# Initialize Virtual Environment
python -m venv venv
source venv/Scripts/activate

# Run the Master Audit Engine
python run_aegis_audit.py
5. Technical Specifications
Language: Python 3.10+

Core Libraries: Pandas (Data Processing), Matplotlib/Seaborn (Visualization), Subprocess (Engine Orchestration).

Data Integrity: UTF-8-SIG encoding for global character support.

Audit Output: CSV, TXT, and PNG assets located in the /reports directory.

6. Compliance Certification
This tool is designed to assist Independent Audit Architects in certifying AI systems as "Low Risk" or "High Risk" under the global regulatory framework for Responsible AI.