import joblib

# Load feature columns
feature_columns = joblib.load("model/feature_columns.pkl")

print("===== FEATURE COLUMNS =====")
for i, col in enumerate(feature_columns, 1):
    print(f"{i}. {col}")