import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as spint

#arr = np.array([1,2,3,4,5])
#print(arr)
#A = np.array([[1,2,3],[7,8,9]])
#print(A)
#A = np.array([[1,2,3],
#              [7,8,9]])
#print(A)
#A = np.array([[1,2, \
#    3],
#              [7,8,9]])
#print(A)
#v = np.arange(1,7)
#print(v,"\n")
#v = np.arange(-2,7)
#print(v,"\n")
#v = np.arange(1,10,3)
#print(v,"\n")
#v = np.arange(1,10.1,3)
#print(v,"\n")
#v = np.arange(1,11,3)
#print(v,"\n")
#v = np.arange(1,2,0.1)
#print(v,"\n")
#v = np.linspace(1,3,4)
#print(v)
#v = np.linspace(1,10,4)
#print(v)
#X = np.ones((2,3))
#Y = np.zeros((2,3,4))
#Z = np.eye(2) # np.eye(2,2) # np.eye(2,3)
#Q = np.random.rand(2,5) # np.round(10*np.random.rand((3,3)))
#print(X,"\n\n",Y,"\n\n",Z,"\n\n",Q)
#U = np.block([[Q], [X,Z]])
#print(U)
#V = np.block([[
#np.block([
#np.block([[np.linspace(1,3,3)],
#[np.zeros((2,3))]]) ,
#np.ones((3,1))])
#],
#[np.array([100, 3, 1/2, 0.333])]] )
#print(V)
#print( V[0,2] )
#print( V[3,0] )
#print( V[3,3] )
#print( V[-1,-1] )
#print( V[-4,-3] )
#print( V[3,:] )
#print( V[:,2] )
#print( V[3,0:3] )
#print( V[np.ix_([0,2,3],[0,-1])] )
#print( V[3] )
#Q = np.delete(V, 2, 0)
#print(Q)
#Q = np.delete(V, 2, 1)
#print(Q)
#v = np.arange(1,7)
##print( np.delete(v, 3, 0) )
##print(np.size(v))
##print(np.shape(v))
##print(np.size(V))
##print(np.shape(V))
#A = np.array([[1, 0, 0],
#[2, 3, -1],
#[0, 7, 2]] )
#B = np.array([[1, 2, 3],
#[-1, 5, 2],
#[2, 2, 2]] )
##print( A+B )
##print( A-B )
##print( A+2 )
##print( 2*A )
#MM1 = A@B
##print(MM1)
#MM2 = B@A
##print(MM2)
#MT1 = A*B
##print(MT1)
#MT2 = B*A
##print(MT2)
#DT1 = A/B
##print(DT1)
#C = np.linalg.solve(A,MM1)
##print(C) 
#x = np.ones((3,1))
#b = A@x
#y = np.linalg.solve(A,b)
##print(y)
#PM = np.linalg.matrix_power(A,2) 
#PT = A**2 
#A.T 
#A.transpose()
#A.conj().T 
#A.conj().transpose()
#A == B
#A != B
#2 < A
#A > B
#A < B
#A >= B
#A <= B
#np.logical_not(A)
#np.logical_and(A, B)
#np.logical_or(A, B)
#np.logical_xor(A, B)
##print( np.all(A) )
##print( np.any(A) )
##print( v > 4 )
##print( np.logical_or(v>4, v<2))
##print( np.nonzero(v>4) )
##print( v[np.nonzero(v>4) ] )
#print(np.max(A))
#print(np.min(A))
#print(np.max(A,0))
#print(np.max(A,1))
#print( A.flatten() )
#print( A.flatten('F') )
#A = np.array([[1,1,1],
#[1,1,0],
#[0,1,1]])
#b = np.array([[3],
#[2],
#[2]])
#x = np.linalg.solve(A, b)
#print(x)
## wyznacznik macierzy
#print(np.linalg.det(A))
## uwarunkowanie macierzy
#print(np.linalg.cond(A))
## macierz odwrotna
#print(np.linalg.inv(A))
#def f1(x):
#    return x**2
#print(f1(2))

#import mojmodul as mm
#print(mm.f2(2))

#f3 = lambda a,x: a*x**3

#f_podcalkowa = lambda x: f1(x) + mm.f2(x) + f3(1,x)
#calka,blad = spint.quad(f_podcalkowa, 0, 1)
#print("calka = "+str(calka))
#print("blad oszacowania = "+str(blad))



#x = [1,2,3]
#y = [4,6,5]
#plt.plot(x,y)
#plt.show()
#x = np.arange(0.0, 2.0, 0.01)
#y = np.sin(2.0*np.pi*x)
#plt.plot(x,y,'r:',linewidth=6)
#plt.xlabel('Czas')
#plt.ylabel('Pozycja')
#plt.title('Nasz pierwszy wykres')
#plt.grid(True)
#plt.show()
#x = np.arange(0.0, 2.0, 0.01)
#y1 = np.sin(2.0*np.pi*x)
#y2 = np.cos(2.0*np.pi*x)
#plt.plot(x,y1,'r:',x,y2,'g')
#plt.legend(('dane y1','dane y2'))
#plt.xlabel('Czas')
#plt.ylabel('Pozycja')
#plt.title('Wykres ')
#plt.grid(True)
#plt.show()
#x = np.arange(0.0, 2.0, 0.01)
#y1 = np.sin(2.0*np.pi*x)
#y2 = np.cos(2.0*np.pi*x)
#y = y1*y2
#l1, = plt.plot(x,y,'b')
#l2,l3 = plt.plot(x,y1,'r:',x,y2,'g')
#plt.legend((l2,l3,l1),('dane y1','dane y2','y1*y2'))
#plt.xlabel('Czas')
#plt.ylabel('Pozycja')
#plt.title('Wykres ')
#plt.grid(True)
#plt.show()

##CW3
#t1=np.arange(1,6)
#t2=np.arange(5,0,-1)
#t3=np.zeros((3,2),int)
#t4=2*np.ones((2,3),int)
#t5=10*np.ones((5,1),int)
#t6=np.arange(-90,-60,10)
#t7=np.block([[t1],[t2]])
#t8=np.block([[t4],[t6]])
#t9=np.block([t3,t8])
#t10=np.block([[t7],[t9]])
#A=np.block([t10,t5])
#print(A)
##CW4
#B = A[1,:]+A[3,:]
#print(B)
##CW5
#C = [np.max(A[:,0]),np.max(A[:,1]),np.max(A[:,2]),np.max(A[:,3]),np.max(A[:,4]),np.max(A[:,5])]
#print(C)
##CW6
#D = np.delete(B,0,0)
#D = np.delete(D,4,0)
#print(D)
##CW7
#np.put(D, np.where(D == 4), 0, mode='clip')
#print(D)
##CW8
#E = np.delete(C, [np.where(C == np.max(C))[0][0], np.where(C == np.min(C))[0][0]],0)
#print(E)
##CW9
#for i in A:
#    if np.min(i) == np.min(A) and np.max(i) == np.max(A):
#        print(i)
##CW10
#print('Tablicowo:')
#print(D*E)

#print('Wektorowo:')
#print(D@E)

##CW11
#def rng_array():
#    array = np.random.random_integers(10, size=(2,2))
#    return(array, np.trace(array))

#print(rng_array())

#CW12
#A=5*np.ones((5,5))
#def zero(X):
#    np.fill_diagonal(X,0)
#    np.fill_diagonal(np.flipud(X),[0])
#    return X
#print(zero(A))

#CW13

#def sum(array):
#    n=np.shape(array)[0]
#    add=0
#    for i in range (0,n):
#        if i%2 == 0:
#            add+=np.sum(array[i])
#    return add

#print(sum(A))

#CW14

#def lambda1(x1):
#    return np.cos(2*x1)
    
#x=np.arange(-10,10,0.1)   
#plt.plot(x,lambda1(x),'r--')
#plt.show()

#CW15

import module 

#plt.plot(x,lambda1(x),'r--',x,module.rownanie(x),'g+')
#plt.show()

#CW17

#plt.plot(x,lambda1(x),'r--',x,module.rownanie(x),'g+',x,(3*lambda1(x)+module.rownanie(x)),'b*')
#plt.show()

#CW18

#a = np.array([[10, 5, 1, 7], 
#            [10, 9, 5, 5], 
#            [1, 6, 7, 3], 
#            [10, 0, 1, 5]])
#b = np.array([[34], 
#            [44], 
#            [25], 
#            [27]])

#x=np.linalg.solve(a,b)
#print(x)

calka, blad = spint.quad(math.sin, 0, 2*math.pi)
print("calka = "+str(calka))
print("blad oszacowania = "+str(blad))