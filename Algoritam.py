import copy
import numpy as np

def pageRank(niz, bP, d):
    red = niz.shape[1] #5 
    #'shape' možemo koristiti jer je matrica kvadratna; shape[0] = shape[1]
    
    vektor = np.ones(red) / red #([0.2, 0.2, 0.2, 0.2, 0.2])
    #'ones' će stvoriti niz veličine 'red' i napuniti ga jedinicama
    
    tempPR = (((1 - d) / red) + (d * niz)) #zbog ovoga je korištena numPy biblioteka
    
    for i in range(brojPonavljanja):
        PR = np.dot(tempPR, vektor)
    
    return PR 

if __name__ == "__main__":
    print("PageRank algoritam\n------------------\n")
    
    matricaSusjedstva = [[0, 0, 0, 0, 1],
              [0.5, 0, 0, 0, 0],
              [0.5, 0, 0, 0, 0],
              [0, 1, 0.5, 0, 0],
              [0, 0, 0.5, 1, 0]] #matrica susjedstva, M(i, j) je veza "j => i", tako da je svaki vektor stupac = 1, tj. zbroj(i, M(i, j)) = 1
    print("Matrica susjedstva:")
    for red in matricaSusjedstva:
        print(red)
    print("\n")
    temp1 = copy.deepcopy(matricaSusjedstva)
    
    numpyNiz = np.array(temp1) #niz iz numpy biblioeteke
    brojPonavljanja = 100 #proizvoljan odabir
    dampingFactor = 0.85 #u suštini proizvoljan, ali se najčešće koristi ova vrijednost
    print("Vektori:")
    print(pageRank(numpyNiz, brojPonavljanja, dampingFactor))