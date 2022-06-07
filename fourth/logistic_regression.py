import random
import numpy as np

# Convert each line in a text file into a list in Python
with open("prices.txt", "r") as a_file:
    data = []
    for line in a_file:
        line_list = line.strip().split(",")
        line_list_float = [float(x) for x in line_list]
        data.append(line_list_float)

number_of_rows_to_check = round(len(data) * 0.85)
random_data = []

# Choose 85% of the rows of data randomly
while len(random_data) < number_of_rows_to_check:
    rand_row = random.choice(data)
    if rand_row not in random_data:
        random_data.append(rand_row)

data_x = np.array([x[:10] + x[11:] for x in random_data])
data_y = np.array([x[10] for x in random_data])


def h(x, w, b):
    return 1 / (1 + np.exp(-(np.dot(x, w) + b)))


w = np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
b = 0
alpha = 0.001

for iteration in range(100000):
    gradient_b = np.mean(1 * (h(data_x, w, b) - data_y))
    gradient_w = np.dot((h(data_x, w, b) - data_y), data_x) * 1 / len(data_y)
    b -= alpha * gradient_b
    w -= alpha * gradient_w

# The remaining 15% of the data - To check
check_list = [row for row in data if row not in random_data]
true_0 = 0
false_1 = 0
false_0 = 0
true_1 = 0

for row in check_list:
    answer = h(np.array([[row[:10] + row[11:]]]), w, b).tolist()[0]  # Calculating answer
    real_value = row[10]

    if real_value == 0:  # No fire station
        if answer[0] <= 0.5:
            true_0 += 1
        else:
            false_1 += 1
    else:
        if answer[0] <= 0.5:
            false_0 += 1
        else:
            true_1 += 1

accuracy = (true_0 + true_1) / (true_0 + true_1 + false_0 + false_1)
print(f"The accuracy is: {accuracy}")


recall_1 = 0
if true_1 + false_0 != 0:
    recall_1 = true_1 / (true_1 + false_0)

print(f"The recall value of existing fire station: {recall_1}")

precision_1 = 0
if true_1 + false_1 != 0:
    precision_1 = true_1 / (true_1 + false_1)

print(f"The precision value of existing fire station: {precision_1}")

# The F-Measure for existing fire station
f_measure1 = 0
if precision_1 + recall_1 != 0:
    f_measure1 = 2*(precision_1*recall_1)/(precision_1 + recall_1)

print(f"The F-Measure for existing fire station: {f_measure1}")
