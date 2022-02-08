class Solution:
    #Time Complexity - O(2^n)
    #Space Complexity - O(n^2)
    result=[]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result=[]
        self.helper(candidates,target,0,list())
        return self.result
    
    def helper(self,candidates,target,index,path):
        #base
        if target==0:
            temp=path.copy()
            self.result.append(temp)
            return
        if target<0 or index==len(candidates):
            return
        #logic
        
        #choose
        path.append(candidates[index])  #action
        self.helper(candidates,target-candidates[index],index,path)   #recurse
        path.pop()   #backtrack  
        
        #not choose
        self.helper(candidates,target,index+1,path)
