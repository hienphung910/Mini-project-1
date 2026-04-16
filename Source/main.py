import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Read data
df = pd.read_csv("../Data/Salary_dataset.csv")

x = df["YearsExperience"].values
y = df["Salary"].values

# 2. Split train/test
split_index = int(len(x) * 0.8)

x_train = x[:split_index]
y_train = y[:split_index]

x_test = x[split_index:]
y_test = y[split_index:]

# 3. Create matrix X for training
X_train = np.column_stack((np.ones(len(x_train)), x_train))
y_train = y_train.reshape(-1, 1)

# 4. Calculate theta by normal formula
# theta = (X^T X)^(-1) X^T y
theta = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train

#Get bias and weight
b = theta[0, 0]
w = theta[1, 0]

print("He so b =", b)
print("He so w =", w)
print(f"Phuong trinh hoi quy: Salary = {w:.2f} * YearsExperience + {b:.2f}")

# 5. Predict on training
y_train_pred = X_train @ theta

# 6. Predict on test
X_test = np.column_stack((np.ones(len(x_test)), x_test))
y_test = y_test.reshape(-1, 1)
y_test_pred = X_test @ theta

# 7. Calculate MSE
train_mse = np.mean((y_train - y_train_pred) ** 2)
test_mse = np.mean((y_test - y_test_pred) ** 2)

print("\nTrain MSE =", train_mse)
print("Test MSE =", test_mse)

# 8. Print predicted results on the test set
print("\nSo sanh du lieu test va du doan:")
for i in range(len(x_test)):
    print(f"YearsExperience = {x_test[i]}, Salary thật = {y_test[i,0]}, Salary dự đoán = {y_test_pred[i,0]:.2f}")
# 9. Chart
plt.figure(figsize=(8, 5))

plt.scatter(x, y, label="Du lieu that")

# Regression line on test set
X_all = np.column_stack((np.ones(len(x)), x))
y_all_pred = X_all @ theta
plt.plot(x, y_all_pred, label="Duong hoi quy")

plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Linear Regression from Scratch")
plt.legend()
plt.grid(True)
plt.show()