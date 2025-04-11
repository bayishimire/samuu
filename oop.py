# parent class or base class called ("cst")
class cst:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # creat object called "IT"
    def it(self):
        print(f"{self.name}{self.age}")
        #child class or derived class tha called ("ICT")
    
class ICT(cst):
    # creat object called "comp"
    def comp(self):
        print(f"{self.name}{self.age}")
#create object called oop 
oop=ICT("BAYISHIMIRESAMUEL VS ERINEST GISUBIZO",20004) 
oop.it()
oop.comp()
# out put BAYISHIMIRESAMUEL VS ERINEST GISUBIZO20004
#BAYISHIMIRESAMUEL VS ERINEST GISUBIZO20004
  