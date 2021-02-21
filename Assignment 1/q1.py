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
print("Sum :-",object1.sum())
print("Max :-",object1.maximum())
print("Mean :-",object1.mean())
print("Meadian :-",object1.median())
print("Mode :-",object1.mode())
print("Standeard Deviation :-",object1.standard_deviation())
freq,array=object1.frequency_distribution()
print("Frequency Distribution Value:-",array)
print("Frequency Distribution Freq :-",freq)