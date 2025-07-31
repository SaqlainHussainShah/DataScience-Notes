# Mean - Average Value
# Median - Middle Value - If there is an even number of data points, the median is the average of the two middle values.
# Mode - Most Frequent Value
# Standard Deviation - Measure of Variability
# Variance - Measure of Data Spread around mean

def mean(list_of_numbers):
    return sum(list_of_numbers)/len(list_of_numbers)

def median(list_of_values):
    list_of_values = sorted(list_of_values)
    n = len(list_of_values)
    if n == 0:
        return None
    elif n % 2 == 0:
        mid = n //2
        return (list_of_values[mid - 1] + list_of_values[mid+1])/2
    else:
        print(n)
        print(n//2)
        return list_of_values[n//2]
    

# print(median([1, 2, 3, 4, 5]))  # Should return 3
# print(median([1, 2, 3, 4, 5, 6]))  # Should return 3.5 
# print(median([]))  # Should return None



def mode(list_of_numbers):
    frequency = {}
    for number in list_of_numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [num for num in frequency if frequency[num] == max_frequency]
    if len(modes) == len(list_of_numbers):
        return None
    return modes

# print(mode([1, 2, 3, 4, 5, 5, 6]))  # Should return [5]
# print(mode([1, 2, 3, 4, 5]))  # Should return None
# print(mode([1, 2, 2, 3, 3, 4, 5]))  # Should return [2, 3]

def variance(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    mean_value = mean(list_of_numbers)
    squared_diffs = [(x-mean_value)**2 for x in list_of_numbers]
    return sum(squared_diffs)/len(list_of_numbers)

# print(variance([1, 2, 3, 4, 5]))  # Should return 2.0
# print(variance([1, 2, 3, 4, 5, 6]))  # Should return 2.9166666666666665
# print(variance([]))  # Should return None

def standard_deviation(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    return variance(list_of_numbers) ** 0.5

# print(standard_deviation([1, 2, 3, 4, 5]))  # Should return 1.4142135623730951
# print(standard_deviation([1, 2, 3, 4, 5, 6]))  # Should return 1.707825127659933
# print(standard_deviation([]))  # Should return None