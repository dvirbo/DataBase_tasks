import numpy as np
import random

# Convert each line in a text file into a list in Python
with open("prices.txt", "r") as a_file:
    data = []
    for line in a_file:
        line_list = line.strip().split(",")
        line_list_float = [float(x) for x in line_list]
        data.append(line_list_float)

number_of_rows_to_check = round(len(data) * 0.75)
random_data = []

# Choose 75% of the rows of data randomly
while len(random_data) < number_of_rows_to_check:
    rand_row = random.choice(data)
    if rand_row not in random_data:
        random_data.append(rand_row)


data_x = np.array([x[:11] for x in random_data])  # 1-11
data_y = np.array([y[11] for y in random_data])  # 12 -> final price

w1 = w2 = w3 = w4 = w5 = w6 = w7 = w8 = w9 = w10 = w11 = 0
b = 0
alpha = 0.001

for iteration in range(1000):
    price = w1 * data_x[:, 0] + w2 * data_x[:, 1] + w3 * data_x[:, 2] + w4 * data_x[:, 3] + \
            w5 * data_x[:, 4] + w6 * data_x[:, 5] + w7 * data_x[:, 6] + w8 * data_x[:, 7] + \
            w9 * data_x[:, 8] + w10 * data_x[:, 9] + w11 * data_x[:, 10] + b

    # Gradients
    gradient_b = np.mean(1 * (price - data_y))
    w1_gradient = np.dot((price - data_y), data_x[:, 0]) * 1.0 / len(data_y)
    w2_gradient = np.dot((price - data_y), data_x[:, 1]) * 1.0 / len(data_y)
    w3_gradient = np.dot((price - data_y), data_x[:, 2]) * 1.0 / len(data_y)
    w4_gradient = np.dot((price - data_y), data_x[:, 3]) * 1.0 / len(data_y)
    w5_gradient = np.dot((price - data_y), data_x[:, 4]) * 1.0 / len(data_y)
    w6_gradient = np.dot((price - data_y), data_x[:, 5]) * 1.0 / len(data_y)
    w7_gradient = np.dot((price - data_y), data_x[:, 6]) * 1.0 / len(data_y)
    w8_gradient = np.dot((price - data_y), data_x[:, 7]) * 1.0 / len(data_y)
    w9_gradient = np.dot((price - data_y), data_x[:, 8]) * 1.0 / len(data_y)
    w10_gradient = np.dot((price - data_y), data_x[:, 9]) * 1.0 / len(data_y)
    w11_gradient = np.dot((price - data_y), data_x[:, 10]) * 1.0 / len(data_y)

    # Update b and w's
    b -= alpha * gradient_b
    w1 -= alpha * w1_gradient
    w2 -= alpha * w2_gradient
    w3 -= alpha * w3_gradient
    w4 -= alpha * w4_gradient
    w5 -= alpha * w5_gradient
    w6 -= alpha * w6_gradient
    w7 -= alpha * w7_gradient
    w8 -= alpha * w8_gradient
    w9 -= alpha * w9_gradient
    w10 -= alpha * w10_gradient
    w11 -= alpha * w11_gradient

# The remaining 25% of the data - To check
check_list = [row for row in data if row not in random_data]

# Loss check
sum = 0
for row in check_list:
    sum += (np.dot(np.array(row[:11]), np.array([w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11])) + b) - row[11]

loss = sum / len(check_list)
print(f"loss: {loss}")