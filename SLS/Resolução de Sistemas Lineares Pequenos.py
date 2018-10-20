# Resolução de Sistemas Lineares Pequenos

"""
Created on Sat Oct 20 12:56:28 2018

@author: Lais Calandrine
"""
# Bibliteca para matrizes, álgebra linear (linalg),...
import numpy as np

# As matrizes
A = np.array([[1,1],[-3,1]])
B = np.array([[6],[2]])

# Encontra o X usando a função solve

X = np.linalg.solve(A,B)

# Resultado para cada variável

print("x = ", X[0])
print("y = ", X[1])
