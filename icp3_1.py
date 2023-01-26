import numpy as np

# Create a random vector of size 20 with float values between 1 and 20
vec = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
vec = vec.reshape(4, 5)

# Replace the max value in each row with 0 (axis=1)
vec[np.arange(4), vec.argmax(axis=1)] = 0

print(vec)
