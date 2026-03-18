class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {} # create the dictionary to store number -> index
        for i in range(len(nums)):
            remaining = target-nums[i]

            if remaining in hash_map:
                return[hash_map[remaining],i]
            hash_map[nums[i]] = i
        
       

