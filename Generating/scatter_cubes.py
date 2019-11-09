import matplotlib.pyplot as plt

# Generate the data.
x_values = list(range(0,100))
y_values = [x**3 for x in x_values]

# Create a scatter plot.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Format the look of the plot.
plt.title("Cubed Numbers", fontsize=20)
plt.xlabel("Values",fontsize=15)
plt.ylabel("Cubes",fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=10)

# Show the graph.
plt.show()