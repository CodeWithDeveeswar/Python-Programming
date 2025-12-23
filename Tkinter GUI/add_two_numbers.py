import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Add 2 Numbers Calculator")
root.geometry("300x200")

# Labels and Entry boxes
tk.Label(root, text="Enter Number 1:").pack(pady=5)
num1_entry = tk.Entry(root)
num1_entry.pack()

tk.Label(root, text="Enter Number 2:").pack(pady=5)
num2_entry = tk.Entry(root)
num2_entry.pack()

# Result Label
result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=10)

# Function to add numbers
def add_numbers():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        total = num1 + num2
        result_label.config(text=f"Result: {total}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Button
tk.Button(root, text="Add", command=add_numbers).pack(pady=5)

# Run the app
root.mainloop()