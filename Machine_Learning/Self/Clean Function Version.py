def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, b = 0, 0
    n = len(X)

    for _ in range(epochs):
        y_pred = m * X + b
        
        dm = (-2/n) * np.sum(X * (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)
        
        m -= lr * dm
        b -= lr * db

    return m, b


# Usage
X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

m, b = gradient_descent(X, y)
print(m, b)