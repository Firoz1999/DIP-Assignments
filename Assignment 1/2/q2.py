from user_func import *
import random 
# let row and col of the matrix r and c
r=5;c=5
rand_matrix=[]
for row in range(r):
    tmp_row=[]
    for col in range(c):
        tmp_row.append(random.randint(0,10))
    rand_matrix.append(tmp_row)


object1=user_define_func(rand_matrix)
print("Matrix :- ")
print("----------------")
object1.print()
print("----------------")
print_table([
    ["Sum :-",object1.sum()],
    ["Max :-",object1.maximum()],
    ["Mean :-",object1.mean()],
    ["Meadian :-",object1.median()],
    ["Mode :-",object1.mode()],
    ["Standeard Deviation :-",object1.standard_deviation()],
],["Defination","Value"],25)
data=[];array,freq=object1.frequency_distribution()
for i in range(len(array)):
    data.append([array[i],freq[i]])
print("Frequency Distribution")
print_table(data,["Value","Frequency"])