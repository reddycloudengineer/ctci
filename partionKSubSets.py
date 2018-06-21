nums=[1,2,3]
k=4

class Solution(object):
    def canPartionKSubsets(self,nums):
        return self.getSubsets(nums,0)
    def getSubsets(self,nums,ind):
        allSubsets=[]
        if len(nums)==ind:
            allSubsets.append([])
        else:
            allSubsets=self.getSubsets(nums,ind+1)
            item=nums[ind]
            newSubsets=[]
            for each in allSubsets:
                newSubsets.append([item]+each)
            newSubsets.extend(allSubsets)
            allSubsets=newSubsets
        return allSubsets





def can_partition(nums):
    sol = Solution()
    d = {}
    for each in sol.canPartionKSubsets(nums):
        s = sum(each)
        if s in d:
            d[s].append(s)
        else:
            d[s] = [each]
    for each in d:
        if len(each)==2:
            return each

    return False


