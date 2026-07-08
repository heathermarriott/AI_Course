from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = load_breast_cancer()
X = data.data
y = data.target
feature_names = data.feature_names

# Create the Random Forest model
model = RandomForestClassifier(random_state=42)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Display accuracy
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred))

# Display feature importances
feature_importance = pd.Series(
    model.feature_importances_,
    index=feature_names
).sort_values(ascending=False)

print("\nFeature Importances:")
print(feature_importance)

# Plot feature importances
plt.figure(figsize=(12, 6))
feature_importance.plot(kind="bar")
plt.title("Random Forest Feature Importances")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
