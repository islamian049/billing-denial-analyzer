"""
Billing Denial Analyzer - By Dr. Rashid Mansoor
Senior Billing Auditor @ Ecodermedico | MBBS
NOTE: Uses synthetic data for portfolio. Real data available on request.
"""
import pandas as pd

def analyze_denials(csv_file):
    print(f"Analyzing: {csv_file}")
    df = pd.read_csv(csv_file)
    
    print("\n--- TOP DENIAL REASONS ---")
    print(df['denial_reason'].value_counts())
    
    print("\n--- TOP DENYING PAYERS ---")
    print(df['payer'].value_counts())
    
    print("\n--- ESTIMATED LOSS ---")
    print(f"Total Denied Amount: ${df['amount'].sum()}")
    
    # Insight from my real experience
    co50 = df[df['denial_reason'] == 'CO-50']
    print(f"\nCO-50 (Non-covered service) Count: {len(co50)} - This was 40% of our denials at Ecodermedico. Fixed by improving Progress Notes documentation.")

# Run with synthetic file
# analyze_denials('sample_denials_synthetic.csv')

# When actual data is needed, I will provide real CSV under NDA
# Contact: syedrashidmansoor049@gmail.com