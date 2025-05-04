# Import required libraries
import pandas as pd
import numpy as np
from pycaret.regression import setup, compare_models, tune_model, save_model, create_model
import warnings
import os

warnings.filterwarnings('ignore')  # Suppress common warnings

# Load the master dataset
master_file_path = 'main_file_updated.csv'  # Use your path
try:
    master_df = pd.read_csv(master_file_path)
except FileNotFoundError:
    print(f"ERROR: Master file not found at {master_file_path}")
    exit()
except Exception as e:
    print(f"ERROR: Could not read master file: {e}")
    exit()

# --- Clean Column Names FIRST ---
print("Cleaning column names...")
original_cols = master_df.columns
master_df.columns = master_df.columns.str.replace('  ', ' ', regex=False)  # Replace double space with single
master_df.columns = master_df.columns.str.strip()  # Remove leading/trailing whitespace
new_cols = master_df.columns
changed_cols = {o: n for o, n in zip(original_cols, new_cols) if o != n}
if changed_cols:
    print("Renamed columns:", changed_cols)
else:
    print("No column names needed renaming.")


# Select features and target
features = [
    'Credits', 'Player Type', 'Team', 'Innings', 'Runs', 'Balls Faced', 'Fours', 'Sixes',
    'Batting Average', 'Strike Rate', 'Boundary_Percentage', 'Innings_X', 'Balls Bowled',
    'Runs_Conceded', 'Wickets', 'Bowling Average', 'Economy Rate', 'Bowling Strike_rate',
    'RECENT_FORM'  # Added RECENT_FORM feature
]
target ='Weighted_Score'

# Filter the dataset to include only the selected features and target
data = master_df[features + [target]].dropna()

# --- PyCaret Setup ---
print("\nSetting up PyCaret experiment...")
try:
    exp_reg = setup(data=data, target=target, session_id=123, normalize=True)
    print("PyCaret setup complete.")

    # --- Model Training and Tuning ---
    print("\nComparing specific models...")
    # Commenting out compare_models to explicitly select models
    # best_model = compare_models()
    # print(f"\nBest model found: {best_model}")

    # Train a few specific models
    lr = create_model('lr')  # Linear Regression
    rf = create_model('rf')  # Random Forest Regressor
    gbr = create_model('gbr') # Gradient Boosting Regressor

    # You can compare the performance of these models here if needed
    print("\nLinear Regression:")
    print(lr)
    print("\nRandom Forest Regressor:")
    print(rf)
    print("\nGradient Boosting Regressor:")
    print(gbr)

    # Let's tune the Gradient Boosting Regressor (you can change this to the model that performs best)
    print("\nTuning the Gradient Boosting Regressor with more iterations...")
    tuned_model = tune_model(gbr, optimize='R2', n_iter=20) # Increased n_iter to 20
    print("\nModel tuning complete.")
    print(tuned_model)

    # --- Save the Model ---
    save_path = os.path.join(os.path.dirname(__file__), 'model')  # Save in same directory as script
    print(f"\nSaving the final tuned model to {save_path}...")
    save_model(tuned_model, save_path)  # Saves the best (original or tuned)

    print("✅ Model training complete. Model saved as 'model'.")

except Exception as e:
    # Generic exception handling
    print("\n❌❌❌ An error occurred during PyCaret setup or training! ❌❌❌")
    import traceback
    print(traceback.format_exc())
    print("\nData Info just before error:")
    print(data.info())
    print("\nFeatures List:")
    print(features)