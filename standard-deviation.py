
import math

import numpy


# def s_deviation(numbers):
#     mean = sum(numbers) // len(numbers)
#     std_diff = sum((num - mean) ** 2 for num in numbers)
#     std_dev = math.sqrt(std_diff / len(numbers))
#     return std_dev


arr = [3, 4, 5, 6, 2, 3, 10, 12, 14, 15, 16]

# result = s_deviation()
# result = numpy.random.uniform(0.0, 5.0, 250)
mean = numpy.std(arr)


print(mean)
