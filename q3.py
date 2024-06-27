import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Define years and months
years = list(range(2020, 2025))
months = list(range(1, 13))

# Generate new expense data
data = []

for year in years:
    for month in months:
        # Generate random expense values with a different mean and standard deviation
        expense = 1500 + np.random.normal(0, 200)
        data.append((year, month, expense))

# Create DataFrame
df = pd.DataFrame(data, columns=["Year", "Month", "Expense"])

# Function to randomly predict expense
def random_predict(df):
    return df["Expense"].sample().values[0]

# Randomly sample 20 rows
random_samples = df.sample(n=20)

# Add a column with random predictions
random_samples["Predicted_Expense"] = random_samples.apply(lambda row: random_predict(df), axis=1)

# Calculate Mean Squared Error (MSE)
mse = np.mean((random_samples["Expense"] - random_samples["Predicted_Expense"]) ** 2)

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)

# Print the sampled DataFrame and the error metrics
print(random_samples)
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
