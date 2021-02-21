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
print("Sum :-",object1.sum())
print("Max :-",object1.maximum())
print("Mean :-",object1.mean())
print("Meadian :-",object1.median())
print("Mode :-",object1.mode())
print("Standeard Deviation :-",object1.standard_deviation())
freq,array=object1.frequency_distribution()
print("Frequency Distribution Value:-",array)
print("Frequency Distribution Freq :-",freq)
