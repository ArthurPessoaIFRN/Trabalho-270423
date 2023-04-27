A = int(input('Bote o primeiro Numero aqui'))
B = int(input('Bota o segundo Numero aqui'))
def Maior(A , B):
 if A < B:
  return B
 if B < A:
  return A
 if B == A:
  return 'Numeros Iguais'

N = Maior(A, B)
print('maior numero é:', N)
