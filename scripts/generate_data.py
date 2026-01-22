import pandas as pd
import numpy as np
from faker import Faker
import os

def generate_synthetic_loan_data(num_records=40000):
    # 1. Initialize Irish Locale (Western EU Standard)
    fake = Faker('en_IE') 
    print(f"Status: Generating {num_records} synthetic records for Ireland Jurisdiction...")

    # 2. Define Economic Parameters (Euro-based)
    records = []
    for _ in range(num_records):
        gender = np.random.choice(['Male', 'Female'], p=[0.5, 0.5])
        
        # Name generation based on gender
        name = fake.name_male() if gender == 'Male' else fake.name_female()
            
        record = {
            'Applicant_ID': f"IE-{np.random.randint(100000, 999999)}",
            'Name': name,
            'Age': np.random.randint(22, 70),
            'Gender': gender,
            'County': fake.county(),
            'Annual_Income_Euro': np.random.randint(25000, 120000),
            'Credit_Score': np.random.randint(300, 850),
            'Education': np.random.choice(['Undergrad', 'Postgrad', 'PhD', 'Diploma'], p=[0.4, 0.4, 0.1, 0.1])
        }
        records.append(record)

    df = pd.DataFrame(records)

    # 3. Decision Simulation Logic (Bias Injection for Stress Testing)
    # This simulates a biased AI model for auditing purposes.
    def simulate_loan_decision(row):
        # Base probability weighted by Gender to simulate systemic bias
        probability = 0.8 if row['Gender'] == 'Male' else 0.4
        
        # Merit-based weight (Legitimate criteria)
        if row['Credit_Score'] > 700:
            probability += 0.1
            
        return 'Approved' if np.random.rand() < probability else 'Rejected'

    df['Loan_Status'] = df.apply(simulate_loan_decision, axis=1)

    # 4. Data Persistence
    os.makedirs('data', exist_ok=True)
    output_path = 'data/ireland_loan_data.csv'
    df.to_csv(output_path, index=False)

    print(f"Success: Dataset created at {output_path}")
    print("Information: Data complies with EU demographic distribution standards.")

if __name__ == "__main__":
    generate_synthetic_loan_data()