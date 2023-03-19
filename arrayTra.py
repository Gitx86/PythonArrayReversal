
class ArrayTrans:
    def __init__(self, array):
        if (type(array)==list):
            self.array = array
        else:
            print('Not compatible array')
            exit()

    def no_of_col(self):
        col_len=len(self.array[0])
        for i in range(self.no_of_row()):
            if len(self.array[i]) != col_len:
                print("Array Shape error")
                exit()
        return(col_len)

    def no_of_row(self):
        return(len(self.array))

    def Transpose(self):
        tempArray=[]
        outputArray=[]
        for c in range(self.no_of_col()):
            for r in range(self.no_of_row()):
                tempArray.append(self.array[r][c])
            outputArray.append(tempArray)
            tempArray = []
        return(outputArray)

def test():
    test2Darray=[['a','b'],['c','d'],['e','f']]
    # test2Darray= ''
    a1 = ArrayTrans(test2Darray)
    print(a1.Transpose())


if __name__ == "__main__":
    test()