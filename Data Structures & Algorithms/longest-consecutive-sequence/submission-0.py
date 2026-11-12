
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_count = 0

        for num in seen:

            if num - 1 not in seen:

                count = 1
                current = num

                while current + 1 in seen:
                    count += 1
                    current += 1

                max_count = max(count, max_count)

        return max_count
