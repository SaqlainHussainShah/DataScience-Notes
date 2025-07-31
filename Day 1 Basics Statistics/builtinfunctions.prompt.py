# Mean - Average Value
# Median - Middle Value - If there is an even number of data points, the median is the average of the two middle values.
# Mode - Most Frequent Value
# Standard Deviation - Measure of Variability
# Variance - Measure of Data Spread around mean

import numpy as np
from scipy import stats as st

def mean(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    return np.mean(list_of_numbers)

# print(mean([1, 2, 3, 4, 5]))  # Should return 3.0
# print(mean([]))  # Should return None
# print(mean([1, 2, 3, 4, 5, 6]))  # Should return 3.5

def median(list_of_values):
    if len(list_of_values) == 0:
        return None
    return np.median(list_of_values)

# print(median([1, 2, 3, 4, 5]))  # Should return 3.0
# print(median([1, 2, 3, 4, 5, 6]))  # Should return 3.5
# print(median([]))  # Should return None

def mode(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    return st.mode(list_of_numbers).mode.tolist()

# print(mode([1, 2, 3, 4, 5, 5, 6]))  # Should return [5]
# print(mode([1, 2, 3, 4, 5]))  # Should return 1
# print(mode([1, 2, 2, 3, 3, 4, 5]))  # Should return [2, 3]

def variance(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    return np.var(list_of_numbers)

# print(variance([1, 2, 3, 4, 5]))  # Should return 2.0
# print(variance([1, 2, 3, 4, 5, 6]))  # Should return 2.9166666666666665
# print(variance([]))  # Should return None

def standard_deviation(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    return variance(list_of_numbers) ** 0.5

print(standard_deviation([1, 2, 3, 4, 5]))  # Should return 1.4142135623730951  
print(standard_deviation([]))  # Should return None
print(standard_deviation([1, 2, 3, 4, 5, 6]))  # Should return 1.707825127659933