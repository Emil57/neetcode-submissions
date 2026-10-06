class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lists = []
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]: continue

            if nums[i] > 0:
                break
            
            l, r = i+1 ,len(nums)-1
            while l<r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0: 
                    lists.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l] == nums[l-1]: l+=1
                    while l<r and nums[r] == nums[r+1]: r-=1
                elif summ > 0: r-=1
                else: l+=1
            
        return lists
