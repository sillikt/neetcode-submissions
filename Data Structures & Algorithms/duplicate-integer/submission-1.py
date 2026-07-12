class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()
        for n in nums:
            if n not in count:
                count.add(n)
            else:
                return True
        return False