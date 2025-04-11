class parentclass:
    def __init__(self,name ,department):
        self.name=name
        self.department=department
    def oop(self):
        return f"{self.name}{self.department} is good name"
class child(parentclass):
    def derved(self):
        return f"{self.name}{self.department} is good  name"
object=child("samuel","ernest")


print(object.derved())     
print(object.oop())        

x = len(object.derved())
print(x )      # Nsamuelernest is goo name
               #samuelernest is goodname
               #24
                 


