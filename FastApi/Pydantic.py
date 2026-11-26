#before  the pydantic 
class Student:
    def __init__ (self,name : str , age: int ,marks: float):
        self.name=name
        self.age=age
        self.marks=marks

s=Student("sanket","23",80)
print(s.name," ",s.age," ",s.marks)
