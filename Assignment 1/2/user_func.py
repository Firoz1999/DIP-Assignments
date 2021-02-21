class user_define_func:
    def __init__(self,matrix):
        self.matrix=matrix
    def print(self):
        for i in self.matrix:
            for j in i:
                print(str(j).ljust(2," "),end=" ")
            print()
        # print()
    def sum(self):
        var=0
        i,j=0,0
        while(i<len(self.matrix)):
            while(j<len(self.matrix[i])):
                var+=self.matrix[i][j]
                j+=1
            i+=1
            j=0
        return var
    def maximum(self):
        var=float("-inf")
        i,j=0,0
        while(i<len(self.matrix)):
            while(j<len(self.matrix[i])):
                if(var<self.matrix[i][j]):
                    var=self.matrix[i][j]
                j+=1
            i+=1
            j=0
        return var
    def mean(self):
        return self.sum()/(len(self.matrix)*len(self.matrix[0]))
    def median(self):
        local_array=[]
        i,j=0,0
        while(i<len(self.matrix)):
            while(j<len(self.matrix[i])):
                local_array.append(self.matrix[i][j])
                j+=1
            i+=1
            j=0
        return sorted(local_array)[round(len(local_array)/2)]
    def mode(self):
        local_array=[]
        freq=[]
        i,j=0,0
        while(i<len(self.matrix)):
            while(j<len(self.matrix[i])):
                if(self.matrix[i][j] not in local_array):
                    local_array.append(self.matrix[i][j])
                    freq.append(1)
                else:
                    freq[local_array.index(self.matrix[i][j])]+=1
                j+=1
            i+=1
            j=0
        
        # return [local_array,freq,local_array[freq.index(max(freq))]]
        return local_array[freq.index(max(freq))]
    def standard_deviation(self):
        local_mean=self.mean()
        local_sum=0
        i,j=0,0
        while(i<len(self.matrix)):
            while(j<len(self.matrix[i])):
                local_sum+=(self.matrix[i][j]-local_mean)**2
                j+=1
            i+=1
            j=0
        local_sum/=(len(self.matrix)*len(self.matrix[0]))
        return local_sum**(1/2)
    def frequency_distribution(self):
        local_array=[]
        freq=[]
        i,j=0,0
        while(i<len(self.matrix)):
            while(j<len(self.matrix[i])):
                if(self.matrix[i][j] not in local_array):
                    local_array.append(self.matrix[i][j])
                    freq.append(1)
                else:
                    freq[local_array.index(self.matrix[i][j])]+=1
                j+=1
            i+=1
            j=0
        return [local_array,freq]
    def __del__(self):
        # print("Destructor calles")
        pass

def print_table(data,label,space=15):
    print("+",end="")
    for _ in range(len(label)):print(space*"-"+"-+",end="")
    print("\n| ",end="")
    for i in label:print(str(i).ljust(space," ")+"| ",end="")
    print("\n+",end="")
    for _ in range(len(label)):print(space*"-"+"-+",end="")
    print()
    for i in range(len(data)):
        print("| ",end="")
        for j in range(len(data[i])):
            print(str(data[i][j]).ljust(space," ")+"| ",end="")
        print()
    if(len(data)>0):
        print("+",end="")
        for _ in range(len(label)):print(space*"-"+"-+",end="")
        print()
