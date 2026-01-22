import os

def run_compliance_audit():
    print("\n[MODULE] Legal Compliance & EU AI Act Engine")
    print("-" * 50)
    
    # Path to the final generated report
    report_path = "reports/AI_Audit_Final_Report.txt"
    
    if os.path.exists(report_path):
        print("Status: Report successfully generated.")
        print(f"Compliance File: {report_path}")
        print("\nNote: The automated mapping of Technical Metrics to EU AI Act Articles")
        print("(Articles 9, 10, 13, and 71) is a Proprietary IP of AEGIS-HUMANITY.")
    else:
        print("Status: Pending Analysis.")
        print("Requirement: Run 'run_aegis_audit.py' with a valid license key.")
    
    print("-" * 50)

if __name__ == "__main__":
    run_compliance_audit()