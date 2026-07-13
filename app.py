from flask import Flask, render_template, request
import joblib
import pandas as pd

# ============================
# Flask App
# ============================

app = Flask(__name__)

# ============================
# Load Model
# ============================

model = joblib.load("model/logistic_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")

print("✅ Model Loaded Successfully")
print("✅ Feature Columns Loaded Successfully")


# ============================
# Home Route
# ============================

@app.route("/")
def home():
    return render_template("index.html")


# ============================
# Prediction Route
# ============================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # -----------------------
        # Read Form Data
        # -----------------------

        pclass = int(request.form["Pclass"])
        sex = request.form["Sex"]
        age = float(request.form["Age"])
        sibsp = int(request.form["SibSp"])
        parch = int(request.form["Parch"])
        fare = float(request.form["Fare"])
        embarked = request.form["Embarked"]
        title = request.form["Title"]
        has_cabin = int(request.form["HasCabin"])

        # -----------------------
        # Feature Engineering
        # -----------------------

        family_size = sibsp + parch + 1

        is_alone = 1 if family_size == 1 else 0

        # -----------------------
        # Empty DataFrame
        # -----------------------

        input_data = pd.DataFrame(
            [[0.0] * len(feature_columns)],
            columns=feature_columns
        )

        # -----------------------
        # Numerical Features
        # -----------------------

        input_data.at[0, "Pclass"] = pclass
        input_data.at[0, "Age"] = age
        input_data.at[0, "SibSp"] = sibsp
        input_data.at[0, "Parch"] = parch
        input_data.at[0, "Fare"] = fare
        input_data.at[0, "FamilySize"] = family_size
        input_data.at[0, "IsAlone"] = is_alone
        input_data.at[0, "HasCabin"] = has_cabin

                # -----------------------
        # One Hot Encoding
        # -----------------------

        # Sex
        if sex == "male":
            input_data.at[0, "Sex_male"] = 1

        # Embarked
        if embarked == "Q":
            input_data.at[0, "Embarked_Q"] = 1

        elif embarked == "S":
            input_data.at[0, "Embarked_S"] = 1

        # C is base category (do nothing)

        # Title
        if title == "Miss":
            input_data.at[0, "Title_Miss"] = 1

        elif title == "Mr":
            input_data.at[0, "Title_Mr"] = 1

        elif title == "Mrs":
            input_data.at[0, "Title_Mrs"] = 1

        elif title == "Rare":
            input_data.at[0, "Title_Rare"] = 1

        # Master is base category (do nothing)

        # -----------------------
        # Prediction
        # -----------------------

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            result = "Likely to Survive"
        else:
            result = "Not Likely to Survive"

        return render_template(
            "index.html",
            prediction=result,
            probability=round(probability * 100, 2)
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction=f"Error: {e}",
            probability=0
        )


# ============================
# Run App
# ============================

if __name__ == "__main__":
    app.run(debug=True)