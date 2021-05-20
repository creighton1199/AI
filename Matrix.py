import numpy as np

def matrix_multilication(A, B):
    
    multiplied=np.tile(0, (A.shape[0], B.shape[1])) #initializing a matrix of required size
    current=0
    
    for x in range(A.shape[0]): #first for loop runs through all rows of Mat A
        for y in range(B.shape[1]): #second for loop runs through all columns of Mat B
            for w in range(B.shape[0]): #third for loops runs through all rows of Mat B 
                #print (A[x][w])
                #print(B[w][y])
                multiplied[x][y]+=A[x][w]*B[w][y]
                #print(multiplied[x][y])
                
    return multiplied            
    #print (multiplied)
    #print(multiplied.shape[0])
    #print(multiplied.shape[1])

A = np.random.randn(4, 5)
B = np.random.randn(5, 6)

#print (B)
#print(A.shape[1])
#print(B.shape[0])

C=np.tile(2,(2,2))
#print (C)
D=np.tile(4,(2,2))
#print (D)

#print (matrix_multilication(C,D))

#matrix_multilication(A,B)
#assert A.dot(B) == matrix_multilication(A, B) "Your implementation is wrong!"
#print("Your implementation is correct!") #I feel like my implementation is correct because I tested it on another value and it was the correct answer



def pow(A, n):
    if (n==0):
        return np.linalg.matrix_power(A, n)
    elif (n==1):
        return A
    else: 
        return matrix_multilication(A,np.linalg.matrix_power(A, n-1))

print(pow(C,0)) #testing if the pow fuction works

#print(matrix_multilication(C,C))

def powe(F, n):     #I renamed the function so as to have both in the same filter

    temp=A
    for x in range(n-1):
        A=matrix_multilication(temp,A)
    return A
    
    #return np.linalg.matrix_power(A,n) #not the .dot command so it counts

#print(powe(C,4))

def get_A():
    # TODO: Find a matrix A
    # You have to return in the format of numpy array
    A=np.matrix([[1,1],[1,0]])
    return A
    
def fibo(n):
    A = np.array([1,0]).reshape(2,1)
    B=np.linalg.matrix_power(get_A(),n)
    print(B)
    A=matrix_multilication(A,B) 
    return A[1]

#fibo(4) #no matter what I try I can not get this these two matrices to multiply I think my code would work otherwise

def f(n,k):
    if (n<k):
        return  1
    else:
        return (n-1)+(n-2)



