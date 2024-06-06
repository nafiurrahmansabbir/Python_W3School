class a:
    def a_method(self):
        print('a')

class b:
    def b_method(self):
        print('b')
    
class i(a,b):
    def i_method(self):
        print('i')
        
        
obj1=i()
obj1.a_method()
obj1.b_method()