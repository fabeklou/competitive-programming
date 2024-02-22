class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Brute force solution sorting and looping:
        #   time O(nlogn)  &  space O(1)
        largest_perim = 0
        length = len(nums)
        nums.sort(reverse=True)

        for i in range(length - 2):
            # For each iteration we get the value of
            #   three sides of a possible triangle
            a, b, c = nums[i:i+3]
            # If the sum of the smallest sides is greather than
            #   the largest side, we have a valid triangle
            if  a < b + c:
                # Since the list is sorted, the first valid triangle
                #   will have the largest perimeter
                largest_perim = a + b + c
                return largest_perim

        return largest_perim
