import binpacking as bp
import numpy as np
import matplotlib.pyplot as plt

# Evaluate how well the 3 different methods work
# (no sorting, increasing order, decreasing order).

# Ask Numpy to generate lots of random sets of items,
# then test the 3 different methods on all of these sets,
# and evaluate the results (how many bins have been used).

# Set up simulation parameters
N_sets = 1000
N_items = 50
bin_capacity = 40
# item_size_limits = [5, 30]
min_size = 5
max_size = 30

# Generate random sets of items
item_sets = np.random.randint(min_size, max_size + 1, (N_sets, N_items))
print(item_sets)

# Start an empty list
N_open_bins = []

# Test the no-sorting method on all the examples
for set_number in range(N_sets):
    bins = bp.first_fit(list(item_sets[set_number, :]), bin_capacity)
    N_open_bins.append(len(bins))

print(N_open_bins)

# Visualise the results
plt.hist(N_open_bins)
plt.show()



# # Testing our function
# items = [2, 1, 3, 2, 1, 2, 3, 1]
# bin_capacity = 4
# bins = bp.first_fit(items, bin_capacity)
# print(bins)  # expected: [4, 4, 4, 3]
