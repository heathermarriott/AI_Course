# Use SKLearn's RandomForestClassifier to create the
# random forest for the should we play tennis question.
#
# ChatGPT assisted with code
#

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset
data = {
    "Outlook":   ["Sunny","Sunny","Overcast","Rain","Rain","Rain","Overcast","Sunny","Sunny","Rain","Sunny","Overcast","Overcast","Rain"],
    "Temperature": ["Hot","Hot","Hot","Mild","Cool","Cool","Cool","Mild","Cool","Mild","Mild","Mild","Hot","Mild"],
    "Humidity":   ["High","High","High","High","Normal","Normal","Normal","High","Normal","Normal","Normal","High","Normal","High"],
    "Wind":       ["Weak","Strong","Weak","Weak","Weak","Strong","Strong","Weak","Weak","Weak","Strong","Strong","Weak","Strong"],
    "PlayTennis": ["No","No","Yes","Yes","Yes","No","Yes","No","Yes","Yes","Yes","Yes","Yes","No"]
}

df = pd.DataFrame(data)

# Encode the target (PlayTennis)
le = LabelEncoder()
y = le.fit_transform(df["PlayTennis"])  # Yes=1, No=0

# Encode features using OneHotEncoder
X = df.drop("PlayTennis", axis=1)

encoder = OneHotEncoder(sparse_output=False)
X_encoded = encoder.fit_transform(X)

# Convert to DataFrame for easier inspection
X_encoded = pd.DataFrame(
    X_encoded,
    columns=encoder.get_feature_names_out(X.columns)
)

# Train the Random Forest
clf = RandomForestClassifier(
    n_estimators=100,     # Number of trees
    criterion="entropy",
    random_state=42,
    max_depth=3
)

clf.fit(X_encoded, y)

# Display feature importances
feature_importance = pd.Series(
    clf.feature_importances_,
    index=X_encoded.columns
).sort_values(ascending=False)

print("Feature Importances:")
print(feature_importance)

# Plot feature importances
plt.figure(figsize=(10,6))
feature_importance.plot(kind="bar")
plt.title("Random Forest Feature Importances")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()

# Example prediction
# Suppose we have a day: Outlook=Sunny, Temp=Cool, Humidity=Normal, Wind=Weak
day = pd.DataFrame([{
    "Outlook": "Sunny",
    "Temperature": "Cool",
    "Humidity": "Normal",
    "Wind": "Weak"
}])

# Transform the new sample with the same encoder
day_encoded = pd.DataFrame(
    encoder.transform(day),
    columns=encoder.get_feature_names_out(X.columns)
)

pred_class_num = clf.predict(day_encoded)
pred_class_label = le.inverse_transform(pred_class_num)

print("Prediction (1=Yes, 0=No):", pred_class_num[0])
print("Predicted class:", pred_class_label[0])
