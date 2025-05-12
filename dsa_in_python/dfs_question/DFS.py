#DFS of tree
#DFS of  directed graph
#DFS of adirected graph

def dfs(index,visited,l1):
    if(l1[index]==None):
          return
    if index>=len(l1):
        return
    visited[index]=True
    print(l1[index],end="->")
    
    if (2*index+1)<len(l1) and visited[2*index+1]!=True:
        dfs(2*index+1,visited,l1)
    if (2*index+2)<len(l1) and visited[2*index+2]!=True:    
        dfs(2*index+2,visited,l1)

if __name__=='__main__':
    l1=[0,1,3,4,2,6,None]
    visited=[False]*7
    print(visited)

    dfs(0,visited,l1);
#this code is by sujal
    
