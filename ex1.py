class Class1:        
    def f_func1(self):
        print ("Метод f_func1() класса Class1")
 
    def f_func2(self):
        print ("Метод f_func2() класса Class1"
 )
class Class2(Class1):
    def f_func3(self):
        print ("Метод f_func3() класса Class2")
c1 = Class2()         
c1.f_func1()         
c1.f_func2()          