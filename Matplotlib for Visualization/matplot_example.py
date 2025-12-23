# What is Matplotlib?
# matplotlib is a library in Python used to create static, animated, and interactive plots.

# The main module:
# pyplot - provides functions to make plots just like MATLAB.

# matplot_example.py
import matplotlib.pyplot as plt
import csv

# Initialize empty lists
months = []
sales = []

# Read CSV file
with open('Matplotlib for Visualization/data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        months.append(row['Month'])
        sales.append(int(row['Sales']))

# Plot the data
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("Matplotlib for Visualization/my_plot.png") # Save as PNG file
plt.show()

