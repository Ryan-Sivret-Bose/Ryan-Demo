
class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print('Feature 1 working')
    
    def feature2(self):
        print('Feature 2 working')

class B(A):

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print('Feature 3 working')
    
    def feature4(self):
        print('Feature 4 working')

a1 = B()