#Дан список чисел. Создать список в который попадают числа, описывающие возрастающую 
#последовательность и содержащие максимальное количество элементов. 
#Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7] Порядок элементов менять нельзя.
 
X = [1, 5, 2, 3, 4, 6, 1, 7]
 
L = []
M = []
j = 1

while j < len(X):
  i = j
  N = X[:]
  while i < len(N)-1:
    if N[i] < N[i+1]: 
      M.append(N[i])
      i += 1
    else:
      N.pop(i+1)    
  j+=1
  if len(L) < len(M):
    L = M
  M=[]

if X[-1] > L[-1]:
  L.append(X[-1])
  
if X[0] < L[0]:
  L.insert(0, X[0])
  
print(L)

#2 Создать и заполнить файл случайными целыми значениями. 
#Выполнить сортировку содержимого файла по возрастанию. 

from random import randint
my_list = [randint(1, 40) for i in range(20)]

my_list.sort() 

my_file = open ('a.txt', 'w')
my_file.write(str(my_list))
my_file.write('  ')
my_file.close