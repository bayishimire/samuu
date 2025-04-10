# class CST:
#     def IT(self,name,age,department):
#         self.name=name
#         self.age=age
#         self.department=department
# #declaration object called (samuel)
# samuel=CST()
# samuel.IT("bayishimire samuel,gisubizo ernest,mr damoul",2004, "informationtechnology")
# print(samuel.name)
# print(samuel.age)
# print(samuel.department)
   





class CST:
    # Constructor to initialize the object
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

# Create an object of the CST class
samuel = CST("Bayishimire Samuel,gisubizo ernest,mr damoul", 224008071, "Information Technology")

# Access and print the object's attributes
print(samuel.name)         # Output: Bayishimire Samuel
print(samuel.age)          # Output: 224008071
print(samuel.department)    # Output: Information Technology
