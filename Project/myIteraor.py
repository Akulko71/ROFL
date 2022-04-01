class MyIterator:
    def __init__(self,number):
        self.number = number

    def __next__(self):
        self.number = self.number ** 2
        return self.number 

    def __iter__(self):
        return self


test = MyIterator(2)
for i in range(1,6): 
    print(next(test))
