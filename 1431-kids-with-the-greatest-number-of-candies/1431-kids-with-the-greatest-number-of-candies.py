class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Brute force solution  time O(n)  &  space O(1)
        
        # the kid with the greatest number of candies before
        # the extra candies are given is our target
        max_candies = max(candies)
        
        # if a the number candies a kid has, added to the number
        # of extra candies is greater than or equal to the max_candies,
        # he will have the greatest number of candies among all the kids
        # if he receives all the extra candies
        for i in range(len(candies)):
            candies[i] = 1 if candies[i] + extraCandies >= max_candies else 0
        
        return candies
