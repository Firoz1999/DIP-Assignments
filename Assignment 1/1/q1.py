from user_func import *
# let the matrix be 
matrix=[
    [1,0,0,1,4],
    [1,0,1,1,0],
    [0,0,14,0,1],
    [1,0,0,7,1],
    [9,0,1,6,0],
]
object1=user_define_func(matrix)
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