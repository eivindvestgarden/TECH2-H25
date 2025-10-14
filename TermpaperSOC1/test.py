import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [10, 15, 7, 12]
values2 = [8, 18, 10, 9]
values3 = [14, 11, 13, 6]

# Bar width
bar_width = 0.2

# X-axis positions for the categories
x = np.arange(len(categories))

# Plotting the bars
plt.bar(x - bar_width, values1, bar_width, label='Series 1')
plt.bar(x, values2, bar_width, label='Series 2')
plt.bar(x + bar_width, values3, bar_width, label='Series 3')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Grouped Bar Chart with Multiple Columns')
plt.xticks(x, categories) # Set x-axis tick labels
plt.legend() # Display the legend
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()