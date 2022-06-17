import numpy as np
import random
import time


Semilla=0
A=np.loadtxt("proyecto\matriz600.txt",dtype="int")# matriz con las m tareas y n subtareas, con n=m
B=np.loadtxt("proyecto\profile600.txt",dtype="int") #profit en [0][x], peso/costo en [1][x]
print(A[0][0])
print(len(B[0]))
def var_decision(X,profit):
    if len(X) ==0:
        X=[0]*len(profit[0])
    return X

def FO(decision,posicion,matriz,profit):#calcula la Funcion Objetivo con dicha decision
    i=0
    aux=0
    while i<len(decision)-1:
        aux=(profit[0][i]*decision[i]*matriz[posicion][i])+aux
        i=i+1
    return aux

def restriccion(decision,peso,matriz,profit):#calcula si dicha decision(variable binaria) cumple la restriccion
    i=0
    aux=0
    while i<len(decision)-1:
        if aux<=peso:
            j=0
            while j<len(decision)-1:
                aux=aux+(profit[1][j]*matriz[j][i]*decision[j])
                j=j+1
        else:
            return 0
        i=i+1
    return 1

def Tareas_resueltas(indice,matriz,profit): #suma cuantas tareas son resueltas en la posicion indice de la matriz
    aux=0
    j=0
    while j<len(profit[0])-1:
        aux=aux+matriz[indice][j]
        j=j+1
    return aux

def probabilidad(prob,profit,matriz):#genera probabilidades segun profit/cantidad de subtareas resuletas en i, si esto es mayor, tiene mas chances de ser escogido
    i=0
    while i<len(profit[0])-1:
        aux=0
        proba=int(profit[0][i]/Tareas_resueltas(i,matriz,profit)) #profit/cantidad de subtareas resueltas, cuanto aporta la realizacion de cada subtarea
        aux=proba
        prob.append(int(aux))
        i=i+1
    return prob

def ruleta_greedy(proba):#Crea un arreglo que se repite m veces una posicion, sirve para seleccionar 1 de las posiciones, la cual sera elegida a la hora de seleccionar una tarea
    probab=[]
    i=0
    global Semilla
    while i<len(proba)-1:
        j=0
        m=proba[i]
        while j<m-1:
            probab.append(i)
            j=j+1
        i=i+1
    random.seed(Semilla)
    aux=random.randint(0,len(probab)-1)
    Semilla=Semilla+1
    seleccion=probab[aux]
    return seleccion

def greedy(matriz,profit,peso):
    i=1
    X=[]
    X=var_decision(X,profit)
    proba=[]
    proba=probabilidad(proba,profit,matriz)
    global Semilla
    while True:
        aux=ruleta_greedy(proba)
        X[aux]=1
        if restriccion(X,peso,matriz,profit)==1:
            break
        elif restriccion(X,peso,matriz,profit)==0:
            print("no hay solucion")
            i=i+1
            break
    return X

def PoblacionInicial(matriz,profit,peso,poblacion):
    i=0
    pob=[]
    start=time.time()
    while i<poblacion:
        pob.append(greedy(matriz,profit,peso))
        i=i+1
    end=time.time()
    print("poblacion "+str(len(pob)))
    print("tiempo greedy "+str(end-start))
        

PoblacionInicial(A,B,109943,100)