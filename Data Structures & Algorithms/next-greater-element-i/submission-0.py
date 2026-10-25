class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mon_stack = []
        next_greater = {}

        for r in range(len(nums2)):
            while mon_stack and mon_stack[-1] < nums2[r]:
                next_greater[mon_stack.pop()] = nums2[r]
            mon_stack.append(nums2[r])
        return [next_greater.get(num, -1) for num in nums1]