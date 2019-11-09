import matplotlib.pyplot as plt

from Generating.random_walk import RandomWalk

# Keep making new walks, prompting as you go.
while True:

    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = plt.cm.Blues, edgecolor='none', s=15)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # Show the plot
    plt.show()

    # Prompt to create another walk
    choice = input("\nDo you want to create another random walk? (y/n):  ")
    choice = choice.lower()
    if choice == 'y':
        # Continue in the loop
        pass
    elif choice == 'n':
        # Stop the program
        break