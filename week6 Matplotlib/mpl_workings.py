import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# lables titles and grid
plt.plot(x, y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("My First Line Chart")
plt.grid(True)
plt.show()

# Line Styles & Markers
plt.plot(x, y, marker='o', linestyle='--')
plt.show()

# Multiple Lines in One Plot
y2 = [15, 18, 22, 35]

plt.plot(x, y, label="Sales 2024")
plt.plot(x, y2, label="Sales 2025")

plt.legend()
plt.show()

# Bar Chart
names = ["A", "B", "C"]
scores = [80, 65, 90]

plt.bar(names, scores)
plt.show()

# Histogram
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.show()

# Scatter Plot
x = [1,2,3,4,5]
y = [5,7,8,5,6]

plt.scatter(x, y)
plt.show()

# Pie Chart
labels = ["Python", "Java", "C++"]
sizes = [60, 25, 15]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()

# subplots
fig, ax = plt.subplots(2, 1)

ax[0].plot(x, y)
ax[0].set_title("Plot 1")

ax[1].plot(x, y) 
ax[1].set_title("Plot 2")
 
plt.tight_layout()
plt.show()

# Figure Size & DPI
plt.figure(figsize=(8, 5), dpi=100)
plt.plot(x, y)
plt.show()

# Saving Plots
plt.plot(x, y)
plt.savefig("output.png")
plt.show()

# Object-Oriented
fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Professional Plot")

plt.show()

# Styling & Themes
plt.style.use("ggplot")
plt.plot(x, y)
plt.show()

