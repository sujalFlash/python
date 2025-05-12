def dfs(i,visited,matrix):
    if i>=len(visited): return
    if visited[i]==True:
        return
    visited[i]=True
    print(i,end="->")
    for current in range(6):
        
        if visited[current]!=True and matrix[i][current]==1:
            dfs(current,visited,matrix)


if __name__=="__main__":
    matrix=[[0]*6]*6
    print(matrix)
    matrix=[[0,0,1,0,0,0],[0,0,0,1,0,0],[0 ,1 ,0 ,0 ,0,0],[0 ,0 ,0 ,0 ,0 ,1],[0 ,0, 0 ,1 ,0 ,0],[0 ,0 ,0,0,0 ,0]]
    visited=[False]*6
    for i in range(0,6):
        dfs(i,visited,matrix)
    
