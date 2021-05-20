import numpy as np

def DFS(A):
    temp=[]
    result = np.pad(A, 1, mode='constant')
    pathway=sfd(result,1,1,temp)
    print(pathway)
    
def sfd(matricks, x, y, travelled): #point 0 is the x coordinate point 1 is the y coordinate
    flag=False
    point=(x,y)
    if ((x==(matricks.shape[0]-2)) and (y==(matricks.shape[1]-2))):
        return travelled
        
    elif ((matricks[x+1][y]==1) and point not in travelled): #start by always going down 
        travelled.append([x+1,y])
        return sfd(matricks,x+1,y,travelled)
        
    elif ((matricks[x][y+1]==1) and point not in travelled): #then always going right
        travelled.append([x,y+1])
        return sfd(matricks,x,y+1,travelled)
        
    elif ((matricks[x-1][y]==1) and point not in travelled): #then check up
        travelled.append([x-1,y])
        return sfd(matricks,x-1,y,travelled)
    
    elif ((matricks[x][y-1]==1) and point not in travelled): #then finally check left
        travelled.append([x,y-1])
        return sfd(matricks,x,y-1,travelled)
    
    elif (travelled==[]): #If there is no available pathway
        return -1
    else:
        travelled.pop()
    

D=np.tile(4,(6,6))
E=np.tile(1,(6,6))
print(D.shape[0])
#print(E.shape[0])



DFS(D)
DFS(E)

visited=[]
queue=[]

def BFS(A):
    result = np.pad(A, 1, mode='constant')  #adds a padding of zeroes arond the matrix so no bound issues
    if (matricks[1,1]==1)
        visited.append([1,1])
        queue.append([1,1]])
    else
        return -1
    
"""def sfb(matricks, x, y):   #I spent hours on this problem and even though I was able to understand how BFS works I was never able to implement it, I'm sorry
    
    point=(x,y)
    queue.pop(0)
    
    if ((x==(matricks.shape[0]-2)) and (y==(matricks.shape[1]-2))): #if it finds the point it will return our visited path
        visited.append(point)
        return visited
    
    elif ((matricks[x+1][y]==1) and point not in visited): #checks if there is a point below then appends it to visited and queue
        visited.apppend([x+1,y])
        queue.append([x+1,y])
        
    elif ((matricks[x][y+1]==1) and point not in visited):
        visited.append([x,y+1])
        queue.append([x,y+1])
    
    elif ((matricks[x-1][y]==1) and point not in visited):
        visited.append([x-1,y])
        queue.append([x-1,y])
        
    elif ((matricks[x][y-1]==1) and point not in visited):
        visited.append([x,y-1])
        queue.append([x,y-1])
    
    elif (queue[]==[])
        return -1
    
    sfb(matricks,queu"""  #then somehow call sfb  again
    
"""Since I was never able to implement BFS I was not able to do the advanced question

    If I was going to do the advanced question I would implement it like this I would either try and find all possible paths, put them in a list, and then add the weight of each node and add them together
    
    The other way that I would potentially try is to always try to go to the shorter heuretic path first on my BFS first then if that path doesnt work I would go to the next shortest one
    
    I'm sorry I could not figure out part two in order to do part three"""




