class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """Алгоритм Бойера-Мура"""
        majority_element = None
        count = 0
        for num in nums:
            if count == 0:
                majority_element = num
            count += 1 if num == majority_element else -1

        return majority_element


test_case = [4,1,2,3,1,2,3,4,2,3,1,4,4]

majority_element = Solution()
print(majority_element.majorityElement(test_case))
