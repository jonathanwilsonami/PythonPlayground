import pandas as pd
import numpy as np
import sys

data1 = [1,2,3,4]
data2 = ["a", "b", "c", "d"]

nums = pd.Series(data1)

# print(nums)

nums2 = np.array([1,2,3,4,5])
nums_series = pd.Series(nums2)
# print(nums_series)

my_fields = ["first", "second", "third", "forth"]
new_series = pd.Series(index = my_fields,
                        data = data1)

print(new_series["first"])