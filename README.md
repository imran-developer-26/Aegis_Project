AEGIS-HUMANITY: Automated AI Audit & Forensic Compliance Suite

AEGIS-HUMANITY is a high-precision forensic auditing framework designed to detect and document systemic gender-based discrimination in financial AI models. Built to align with EU AI Act standards, this suite provides automated bias detection, visual intelligence, and verifiable peer-matching evidence to ensure algorithmic accountability.

Key Features
Forensic Evidence Extraction: Moves beyond percentages to identify specific "Victim vs. Peer" cases.

EU AI Act Alignment: Automated mapping of technical failures to Articles 9, 10, and 13.

Visual Intelligence: Generates high-fidelity heatmaps and parity charts for stakeholders.

Enterprise Scalability: Capable of auditing thousands of records in seconds with zero data-integrity loss.

Module,Purpose,Key Output
A. Data Factory,"Simulates 40,000+ loan applications with Irish demographic distributions.",ireland_loan_data.csv
B. Visual Suite,Generates distribution charts and regional bias heatmaps.,global_bias.png
C. XAI Engine,Analyzes if 'Gender' is illegally influencing model decisions.,Feature Importance Logs
D. Legal Engine,Translates technical findings into legal verdicts for regulators.,legal_summary.txt
E. Audit Logger,Calculates Disparate Impact Ratio (DIR) and Risk Scores.,Technical Audit Logs
F. Forensic Engine,The Heart of AEGIS. Performs Peer-Contrast matching for evidence.,forensic_evidence.csv

Forensic Methodology: "The Peer-Contrast Logic"
Unlike traditional tools that provide abstract statistics, AEGIS-HUMANITY utilizes Direct Evidence Extraction:

Identify Victim: Filters for Females with high Credit Scores (700+) who were Rejected.

Scan for Peer: Searches the database for Males with equal or lower Credit Scores who were Approved.

Audit Trail: Generates a human-readable forensic trail for legal submission.

Installation & SetupTo run the demo and generate audit reports, follow these steps:Bash# Clone the repository
git clone https://github.com/imran-developer-26/aegis-project.git

# Initialize Virtual Environment
python -m venv venv
source venv/Scripts/activate  # On Windows: .\venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run the Master Audit Engine
python run_aegis_audit.py

Technical SpecificationsLanguage: Python 3.10+Core Stack: Pandas, Matplotlib, Seaborn.Standards: ISO/IEC 42001 & EU AI Act Compliance Framework.

Intellectual Property NoticeThe core Forensic Engine Logic and Proprietary Bias Injection Algorithms are protected assets. This public repository serves as a Technical Portfolio. For enterprise licensing or a full-scale private demo, please contact the lead developer.

Lead AI Audit Architect: Imran Hossain : https://github.com/imran-developer-26

Expertise: Responsible AI, Forensic Data Auditing, Compliance Engineering.