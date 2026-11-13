class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=set()
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    res.add((nums[i],nums[left],nums[right]))
                    left=left+1
                    right=right-1
                elif total>0:
                    right=right-1
                elif total<0:
                    left=left+1

        return list(res)

        