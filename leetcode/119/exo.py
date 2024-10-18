def pascal_triangle(n):
    if n==0:
        return []
    if n==1:
        return [[1]]
    if n==2:
        return [[1],[1,1]]
    if n==3:
        return [[1],[1,1],[1,2,1]]
    else:
        triangle=[[1],[1,1],[1,2,1]]
        for a in range(4,n+1):
                l=[1]
                for i in range(1,a):
                    l.append(triangle[a-1][i-1]+triangle[a-1][i])
                l.append(1)
                triangle.append(l)
                
        return triangle[n]
                    
                