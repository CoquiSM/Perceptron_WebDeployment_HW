import numpy as np
import pandas as pd
import random

## got this code so I did not hand make 100 images

def make_shape(shape_type):
    # Start with a blank 5x5 canvas (all 0s)
    grid = np.zeros((5, 5))

    if shape_type == "L":
        grid[:, 0] = 1  # Draw vertical line down the left
        grid[4, :] = 1  # Draw horizontal line across the bottom
        label = 1  #  1 represents "L"

    elif shape_type == "T":
        grid[0, :] = 1  # Draw horizontal line across the top
        grid[:, 2] = 1  # Draw vertical line down the middle
        label = 0  # 0 represents  "T"

    # Add "noise" to make the data realistic
    # This randomly flips 1 or 2 pixels (0 becomes 1, 1 becomes 0)
    for _ in range(random.randint(1, 2)):
        row, col = random.randint(0, 4), random.randint(0, 4)
        grid[row, col] = 1 - grid[row, col]

        # Flatten the 5x5 grid into a single line of 25 numbers
    return grid.flatten(), label


data = []

# Generate 50 'L's and 50 'T's
for _ in range(50):
    pixels, label = make_shape("L")
    data.append(list(pixels) + [label])

for _ in range(50):
    pixels, label = make_shape("T")
    data.append(list(pixels) + [label])

# Create friendly column names (pixel_1, pixel_2 ... pixel_25, label)
columns = [f"pixel_{i + 1}" for i in range(25)] + ["label"]

# Turn it into a DataFrame, shuffle the rows so they are mixed up, and save it
df = pd.DataFrame(data, columns=columns)
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv("shapes_data.csv", index=False)

print("Success! Created 'shapes_data.csv' with 100 images.")
