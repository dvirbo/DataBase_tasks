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
for _ in range(number_of_rows_to_check):
    rand_row = random.choice(data)
    if rand_row not in random_data:
        random_data.append(rand_row)


data_x = np.array([x[:11] for x in random_data])  # 1-11
data_y = np.array([y[11] for y in random_data])  # 12 -> final price

w1 = w2 = w3 = w4 = w5 = w6 = w7 = w8 = w9 = w10 = w11 = 0
b = 0
alpha = 0.001

for iteration in range(100):
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
for row in check_list:
    print(row)
    answer = np.dot(np.array(row[:11]), np.array([w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11])) + b
    print(answer)


# Results - compare most right index to answe
"""
[4.9176, 1.0, 3.472, 0.998, 1.0, 7.0, 4.0, 42.0, 3.0, 1.0, 0.0, 25.9] -> 29.065811978941447
[5.0208, 1.0, 3.531, 1.5, 2.0, 7.0, 4.0, 62.0, 1.0, 1.0, 0.0, 29.5] -> 29.27474788891235
[5.0597, 1.0, 4.455, 1.121, 1.0, 6.0, 3.0, 42.0, 3.0, 1.0, 0.0, 29.9] -> 28.10962288042583
[16.4202, 2.5, 9.8, 3.42, 2.0, 10.0, 5.0, 42.0, 2.0, 1.0, 1.0, 84.9] -> 58.97053366560415
[14.4598, 2.5, 12.8, 3.0, 2.0, 9.0, 5.0, 14.0, 4.0, 1.0, 1.0, 82.9] -> 61.20765856380875
[5.8282, 1.0, 6.435, 1.225, 2.0, 6.0, 3.0, 32.0, 1.0, 1.0, 0.0, 35.9] -> 30.717458068881974
[5.3003, 1.0, 4.9883, 1.552, 1.0, 6.0, 3.0, 30.0, 1.0, 2.0, 0.0, 31.5] -> 27.539965544752235
[8.2464, 1.5, 5.15, 1.664, 2.0, 8.0, 4.0, 50.0, 4.0, 1.0, 0.0, 36.9] -> 37.447703160225785
[9.0384, 1.0, 7.8, 1.5, 1.5, 7.0, 3.0, 23.0, 3.0, 3.0, 0.0, 43.9] -> 27.825803350963973
[5.9894, 1.0, 5.52, 1.256, 2.0, 6.0, 3.0, 40.0, 4.0, 1.0, 1.0, 37.5] -> 30.904784923735384
[8.3607, 1.5, 9.15, 1.777, 2.0, 8.0, 4.0, 48.0, 1.0, 1.0, 1.0, 38.9] -> 44.16653798727258
[8.14, 1.0, 8.0, 1.504, 2.0, 7.0, 3.0, 3.0, 1.0, 3.0, 0.0, 36.9] -> 28.814489975743456
[9.1416, 1.5, 7.3262, 1.831, 1.5, 8.0, 4.0, 31.0, 4.0, 1.0, 0.0, 45.8] -> 36.59425264812775
[12.0, 1.5, 5.0, 1.2, 2.0, 6.0, 3.0, 30.0, 3.0, 1.0, 1.0, 41.0] - > 45.55598567318023
"""