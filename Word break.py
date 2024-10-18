from typing import List
class Solution:
    def wordBreak(self,s:str,wordDict:List[str])->bool:
        n=len(s)+1
        dp=[0]*n
        dp[0]=True
        trues=[0]
         
        for i in range(n):
           for j in range(i):
              if dp[j] and s[j:i] in wordDict:
                 dp[i]=True
                 trues.append(i)
                 break
        return dp[-1]

s=Solution()
print(s.wordBreak("leetcode",['leet','code']))