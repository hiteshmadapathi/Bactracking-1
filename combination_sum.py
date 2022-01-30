class Solution:
    '''
    #Time Complexity - O(n)
    #Space Complexity - O(n)
    result=[]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result=[]
        self.helper(candidates,target,0,list())
        return self.result
    
    def helper(self,candidates,target,index,path):
        #base
        if target==0:
            temp=path+[]
            self.result.append(temp)
            return
        if target<0 or index==len(candidates):
            return
        #logic
        #not choose
        self.helper(candidates,target,index+1,path)
        #choose
        path.append(candidates[index])  #action
        self.helper(candidates,target-candidates[index],index,path)   #recurse
        path.pop()   #backtrack'''   
        
        
    
    #Time Complexity - O(n^2)
    #Space Complexity - O(n^2)
    result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result=[]
        self.helper(candidates,target,0,[])
        return self.result
    
    def helper(self,candidates,target,index,path):
        #base
        if target==0:
            self.result.append(path)
            return
        if target<0 or index==len(candidates):
            return
        #logic
        #not choose
        self.helper(candidates,target,index+1,path)
        #choose
        temp=path+[]
        temp.append(candidates[index])
        self.helper(candidates,target-candidates[index],index,temp)
