import matplotlib.pyplot as plt

x = ['Apple', 'Banana', 'Grapes']
y = [30, 15, 45]

plt.bar(x, y, color='green')
plt.title("Simple Bar Chart")
plt.ylabel("Count")
plt.show()