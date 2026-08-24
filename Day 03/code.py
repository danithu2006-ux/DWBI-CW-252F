import pandas as pd

# 1. Load the dataset
file_name = "AL.csv"
try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_name)
    print(f"Successfully loaded '{file_name}'!\n")
    
    # 2. Basic Information
    print("--- Dataset Shape ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")
    
    print("--- Column Data Types & Non-Null Counts ---")
    df.info()
    
    # 3. Preview the Data
    print("\n--- First 5 Rows ---")
    print(df.head())
    
    # 4. Missing Values Check
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    
    # 5. Summary Statistics for numerical columns
    print("\n--- Summary Statistics ---")
    print(df.describe(include='all'))

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found in the current directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
