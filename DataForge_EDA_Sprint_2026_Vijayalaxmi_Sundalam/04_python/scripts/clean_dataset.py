import pandas as pd
import numpy as np
import os

def run_cleaning_pipeline():
    # 📍 Dynamically find the absolute path of this script file
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # Point to 04_python/scripts/
    WORKSPACE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..")) # Steps back to project root
    
    # 📦 Form safe, absolute target locations
    input_path = os.path.join(WORKSPACE_ROOT, "01_data", "raw", "dataset_raw.csv")
    output_clean = os.path.join(WORKSPACE_ROOT, "01_data", "processed", "dataforge_cleaned.csv")
    output_agg = os.path.join(WORKSPACE_ROOT, "01_data", "processed", "region_sales_aggregated.csv")
    
    if not os.path.exists(input_path):
        print(f"Error: Target data file not found at path:\n{input_path}")
        return

    print(f"Success! Loading dataset from: {input_path}")
    df = pd.read_csv(input_path)
    
    # Prune columns missing above 50%
    df.drop(columns=[c for c in df.columns if df[c].isnull().mean() > 0.50], inplace=True)
    df.drop_duplicates(inplace=True)
    
    # Vectorized Imputations
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna("Unknown")
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].median())
        
    # Cast Temporal Fields
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
    
    # Feature Injections
    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month'] = df['Order Date'].dt.month
    df['Shipping Delay'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['Total Profit'] = df['Sales'] * 0.15
    
    # Group Aggregations
    region_summary = df.groupby('Region', as_index=False)['Sales'].mean()
    region_summary.rename(columns={'Sales': 'Average_Sales_Per_Region'}, inplace=True)
    
    # Write to Disk safely creating missing subfolders
    os.makedirs(os.path.dirname(output_clean), exist_ok=True)
    df.to_csv(output_clean, index=False)
    region_summary.to_csv(output_agg, index=False)
    print("\n\nProduction-level automated dataset parsing sequence concluded.")

if __name__ == "__main__":
    run_cleaning_pipeline()