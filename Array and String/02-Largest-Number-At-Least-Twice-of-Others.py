class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        m_index = nums.index(m)
        for n in nums:
            if(n != m and m < n * 2):
                return(-1)
        return(m_index)