
# Use Sliding Window
def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_ones = 0
        for i in nums:
            if i:
                count += 1
            else:
                count = 0
            if count > max_ones:
                max_ones = count
        return(max_ones)
        