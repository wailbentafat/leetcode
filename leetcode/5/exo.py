class solution:
    def longestpolindrom( self ,s: str) ->str:
       i=0
       ln =len(s)
       for i in range(ln):
           j=i+1
           for j in range(ln):
               if s[i]==s[j]:
                    a=j
                    while a>i:
                       k=k+s[a]
                       a=a-1
                    l=[s[i:j]] 
                    if l==i:
                        return l
                    else:
                        break
                     
               else:  
                   continue
               
                    
                   
                   
                  
                  
       
        
        
solution=solution(
)        
print(solution.longestpolindrom("babad"))