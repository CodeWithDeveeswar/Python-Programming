# Tkinter is the standard GUI (Graphical User Interface) library for Python.
# It lets you build windows, buttons, labels, text boxes, and more — just like apps with a user interface.

# Built-in with Python (no need to install separately)
# Good for building simple desktop applications
# Cross-platform (works on Windows, macOS, Linux)

# tkinter_example.py
import tkinter as tk # Import the tkinter module

# Step 1: Create the main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200") # Set width x height

# Step 2: Add a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20) # Add vertical padding

# Step 3: Add a button
def on_click():
    label.config(text="You clicked the button!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Step 4: Start the GUI loop
root.mainloop()




