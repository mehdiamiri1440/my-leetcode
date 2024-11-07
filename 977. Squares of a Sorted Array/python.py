class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for index,item in enumerate(nums):
            diff=target-item
            if diff not in result:
                result[item]=index
            else:
                return [index,result[diff]]
        
