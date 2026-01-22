import os
import subprocess
import time

def execute_module(module_name, script_path):
    print(f"\nTask: Starting {module_name}...")
    
    # Locate virtual environment python executable
    python_exe = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")
    if not os.path.exists(python_exe):
        python_exe = "python"

    # Security Check: Ensure script exists (Protects proprietary logic)
    if not os.path.exists(script_path):
        print(f"Information: {module_name} is a proprietary module and not included in the public repository.")
        return

    try:
        subprocess.run([python_exe, script_path], check=True)
        print(f"Status: {module_name} completed successfully.")
    except Exception as e:
        print(f"Error: Failure occurred in {module_name}. Details: {e}")

def main():
    start_time = time.time()
    
    print("----------------------------------------------------------")
    print("AEGIS-HUMANITY: AUTOMATED AUDIT SYSTEM (STANDARDIZED VERSION)")
    print("----------------------------------------------------------")

    # Core Execution Flow
    execute_module("Data Factory Simulation", "scripts/generate_data.py")
    execute_module("Visual Intelligence Suite", "scripts/visualize_bias.py")
    
    # Proprietary Modules
    print("\nProcessing Enterprise Compliance Modules...")
    execute_module("Advanced Model Audit (XAI)", "scripts/advanced_audit.py")
    execute_module("Legal Verdict Generation", "scripts/legal_compliance_audit.py")
    execute_module("Technical Audit Logging", "scripts/final_audit_tool.py")

    # Forensic Core
    execute_module("Factual Forensic Evidence Engine", "scripts/final_forensic_audit.py")

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("\n" + "-"*58)
    print(f"SUMMARY: FULL AUDIT CYCLE COMPLETED IN {total_time} SECONDS")
    print("RESTRICTION: Full forensic trace-logs are available in the licensed version only.")
    print("----------------------------------------------------------")

if __name__ == "__main__":
    main()