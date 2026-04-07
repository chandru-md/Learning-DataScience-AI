import numpy as np

# Sample dataset
X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])  # y = 2x + 1

# Initialize parameters
m = 0  # slope
b = 0  # intercept
lr = 0.01  # learning rate
epochs = 1000
n = len(X)

for i in range(epochs):
    y_pred = m * X + b
    
    # Compute gradients
    dm = (-2/n) * np.sum(X * (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)
    
    # Update parameters
    m = m - lr * dm
    b = b - lr * db

# Final result
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")