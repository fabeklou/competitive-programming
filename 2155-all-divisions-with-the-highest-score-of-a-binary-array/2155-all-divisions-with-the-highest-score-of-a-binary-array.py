class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # Brute force approach
        # time O(n*n)  &  space O(n)
        """
        max_ = 0
        dss = []  # division scores

        for i in range(len(nums) + 1):
            # add number of zeros in the left subarray
            # to the number of ones in the right subarray
            ds = nums[:i].count(0) + nums[i:].count(1)
            max_ = max(max_, ds)
            dss.append(ds)

        return [i for i, value in enumerate(dss) if value == max_]
        """
        
        # Oprimized solution
        # time O(n) & space O(n)
        dss = []
        ones = sum(nums)
        max_score = ones
        zeros = 0
    
        for i in range(len(nums) + 1):
            if i == 0:
                dss.append(ones)
                continue

            if nums[i-1] == 0:
                zeros += 1
            else:
                ones -= 1
            
            max_score = max(max_score, zeros+ones)
            dss.append(zeros + ones)
        
        return [i for i, v in enumerate(dss) if v == max_score]      
