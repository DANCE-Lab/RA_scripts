import random
import string
import pandas as pd
import numpy as np
import csv 

def generate_id(seed):
    # Seed the random number generator
    random.seed(seed)
    # Generate first 5 characters as digits
    digits_part = ''.join(random.choices(string.digits, k=5))
    # Generate the last character as an uppercase letter
    letter_part = random.choice(string.ascii_uppercase)
    # Combine both parts
    return digits_part + letter_part

# Seed for reproducibility
seed_value = 12345

# Generate 100 IDs
id_list = [generate_id(seed_value + i) for i in range(100)]

# Save the IDs to a CSV file
csv_file = "participant_ids.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Participant_ID_Number"])
    # Write the IDs
    for id_number in id_list:
        writer.writerow([id_number])

print(f"IDs saved to {csv_file}")
