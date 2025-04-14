# class cst:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def it(self):
#         print(f"{self.name} {self.age}")

# class ICT(cst):
#     def __init__(self, name, age):
#         super().__init__(name, age)  # Call the parent class constructor use "super()"

#     def comp(self):
#         print(f"{self.name} {self.age}")

# # Create object from child class
# oop = ICT("BAYISHIMIRESAMUEL VS ERINEST GISUBIZO", 20004)

# # Call methods
# oop.it()
# oop.comp()
import pandas as pd
data={"name":["bay","samu"],"age":[23,34]}
df=pd.DataFrame(data)
print("name and age")
print(df.to_string(index=False))


                 


