#before  the pydantic 
class Student:
    def __init__ (self,name : str , age: int ,marks: float):
        self.name=name
        self.age=age
        self.marks=marks

s=Student("sanket","23",80)
print(s.name," ",s.age," ",s.marks)

print("-"*30)

#after pydantic
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    salary: float

s = Student(name="ram",age=22,salary=80000.0)
print(s)

#s2 = Student(name=99,age="22",salary=True)
#print(s2)

print("-"*30)
#strict mode in pydantic

from pydantic import BaseModel,ConfigDict

class student(BaseModel):
    model_config = ConfigDict(strict=True)
    age : int

s = student(age=22)

print(s)

print("-"*30)

#lax mode in pydantic

from pydantic import BaseModel

class Students(BaseModel):
    age : int

s = Students(age="23")

print(s)
print(type(s.age))

print("-"*40)

#real world approch when data is come in dictionary formate

data = {
    "name":"sham",
    "age":24,
    "salary":30000
}

s3 = Student(**data)
print(s3)


print("-"*50)

data1={
    "name":"kalash",
    "age":23.4,
    "salary":"500000"
}

# s5 = student(**data1)
# print(s5)
'''Traceback (most recent call last):
  File "S:\vs_code\github_repository\FastApi\Pydantic.py", line 76, in <module>
    s5 = student(**data1)
  File "S:\vs_code\.new_env\Lib\site-packages\pydantic\main.py", line 280, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for student
age
  Input should be a valid integer [type=int_type, input_value=23.4, input_type=float]
    For further information visit https://errors.pydantic.dev/2.14/v/int_type'''

#use booliean value in that

class check(BaseModel):
    name : str
    age : int
    player : bool

s4 = check(name="ram",age=45,player="no")
print(s4)

print("->"*40)

#validation error

from pydantic import ValidationError

data2 = {
    "name":12,
    "age":"sixty"
}

try:
    ss = Student(**data2)
except ValidationError as e:
    print(f"number of error : {e.error_count()}")
    for err in e.errors():
        print(f" Field : {err["loc"]} , type : {err["type"]} , Massage : {err["msg"]}")


# from pydantic import BaseModel

# class check(BaseModel):
#     product_id: int = "abc"

# s = check()
# print(s)

# from pydantic import BaseModel, Field

# class Check(BaseModel):
#     product_id: int = Field(default="abc", validate_default=True)

# s = Check()
# print(s)
'''------------------------------------------------------------------------------------------------'''
'''Try writing a small Product (BaseModel) in your notebook with fields: product id: int, name: str, price: float, in_stock: bool,
and test it with:
Valid coerced inputs (product_id="50", price="199,99", in_stock="1"),
A broken input inside try / except ValidationError as et and print e.error_count(),'''
print("<>"*50)
from pydantic import BaseModel

class product(BaseModel):
    product_id : int
    name : str
    price : float
    in_stock : bool

data3 = {
    "product_id" : "50",
    "price" : "199,99",
    "in_stock" : "1"
}

try:
    quest = product(**data3)

except ValidationError  as e:
    print(f"number of error in code : {e.error_count()}")
    for err in e.errors():
        print(f" field : {err["loc"]}, type :{err["type"]} , massage : { err["msg"]}")


print("->"*50)

# required as non-nullabel
#what happen when value not provide
from pydantic import BaseModel,ValidationError

class pro(BaseModel):
    product_id : int
    name : str


values = {
    "product_id" : 123
}

try:
    p = pro(**values)

except ValidationError as e:
    print(f"find the number of errror in that case : {e.error_count()}")
    for err in e.errors():
        print(f" fields : {err["loc"]} , type : {err["type"]}, masssgae : {err['msg']}")

print("-"*40)
#non nullable exp2
#when we are giving none  as a value in dict

val = {
    "product_id" :2321,
    "name":None
}

try:
    p1 = pro(**val)
except ValidationError as e:
    print(f"find the number of error in that case : {e.error_count()}")
    for err in e.errors():
        print(f"field : {err["loc"]} , type : {err["type"]} , massgage: {err['msg']}")

print("<-"*40)

#nullable cocept

#when the none vlaue is not given in dict

from pydantic import BaseModel,ValidationError

class pro1(BaseModel):
    product_id : int
    name : str | None


val2= {
    "product_id": 6932
}

try:
   p3 = pro1(**val2)
except ValidationError  as e:
    print(f"number of error is found in that case : {e.error_count()}")
    for err in e.errors():
        print(f"field : {err["loc"]} , type : {err["type"]} , massage : {err["msg"]}")


print("->"*30)
#exp2
val3= {
    "product_id": 6932,
    "name":None
}

try:
   p3 = pro1(**val3)
except ValidationError  as e:
    print(f"number of error is found in that case : {e.error_count()}")
    for err in e.errors():
        print(f"field : {err["loc"]} , type : {err["type"]} , massage : {err["msg"]}")
'''it is not giving error because the None is placed by the name value location'''



print("-<>-"*15)

#optinal non nullable
#when we give the default value
from pydantic import BaseModel,ValidationError

class op(BaseModel):
    product_id : int
    name : str = "sham"

val4 = {
    "product_id":32123
}

try:
    p2 = op(**val4)
    print(p2)
except ValidationError as e:
    print(f"find the number of error in that case : {e.error_count()}")
    for err in e.errors():
        print(f"field : {err['loc']} , type : {err['type']}, masssgae : {err["msg"]}")
    
print(">-"*20)

#optional nullable
#when we did not give the variable in dictionary and give the none value in class
from pydantic import BaseModel,ValidationError

class op2(BaseModel):
    product_id : int
    name : str | None = None

val5 = {
    "product_id" : 23423
}
try:
    p4 = op2(**val5)
    print(p4)
except ValidationError  as e:
    print(f"number of error occured in the code : {e.error_count()}")
    for err in e.errors():
        print(f"field : {err["loc"]}, type : {err["type"]}, massgage : {err["msg"]}")
#not give errror

val6 = {
    "product_id":23423,
    "name":None
}

try:
    p5 = op2(**val6)
    print(p5)
except ValidationError as e:
    print(f"number of error count : {e.error_count()}")
    for i in e.errors():
        print(f"field :{i['loc']}, type : {i['type']}, massage : {i["msg"]}")
#it is also not give errror because None is given 
#
print("*|*"*20)
#if we give default value in variable pydantic does not validate the given default value 
#exp
class checked(BaseModel):
    name : str = "abc"

checkes = checked()
print(checkes)

print("_"*30)
from datetime import datetime, UTC
import time
class Badexample(BaseModel):
    created_dt : datetime =datetime.now(UTC)

b = Badexample()
time.sleep(2)
b1 = Badexample()

print(b)
print(b1)


print("->"*20)
from uuid import UUID , uuid4
from datetime import datetime, UTC
from pydantic import BaseModel , Field
import time 

class Goodexample(BaseModel):
    request_id : UUID = Field(default_factory = uuid4)
    created_id : datetime = Field(default_factory =lambda : datetime.now(UTC))

k1=Goodexample()
time.sleep(2)
k2=Goodexample()

print(k1)
print(k2)

print(k1.created_id == k2.created_id) # it always False

print("<-"*20)

#example in real life for chatbot

from datetime import datetime, UTC
from pydantic import BaseModel,Field
from uuid import UUID ,uuid4

class chatbot(BaseModel):
    #required
    promt : str
    #optional defaults 
    model : str = "gpt-4o-mini"
    tempratuer : float | None = None
    token : int | None = None  #None = let provide model
    #default
    system_prompt : str | None = None
    stop_sequence : list[str] = Field(default_factory=list)
    #auto genrated meta data request
    created_dt : UUID =Field(default_factory=uuid4)
    requested_dt : datetime = Field(default_factory=lambda: datetime.now(UTC))

req=chatbot(promt="expalin python")
print(req)

req.stop_sequence.append("Hello World!")
print(req)

print("-|-"*10)
from pydantic import BaseModel,Field

class prompt(BaseModel):
    text : str = Field(description="text value")
    user_id : str = Field(...,description='user_id is mendatory')#... means mendatory you will give value at the object created
    value : str | None = Field(default=None , description="value wil given")

print(prompt(text="sank",user_id = "abs"))
# print(prompt(user_id="asc",value="mno"))

print(prompt(text = "kolte",user_id="abc",value="xyz"))

print("~"*20)

# how to validate default value
class validate(BaseModel):
    age : int =  Field(default="abc" , validate_default=True)

try:
    s=validate()
    print(s.age)
except ValidationError as e:
    print(e.errors()[0]["msg"])

print(" >>>"*30)

#dyanamically validate data

class modeldata(BaseModel):
    model_name : str
    version : int = 1
    attribute_val : str = Field(default_factory=lambda x:f"{x["model_name"]}:{x["version"]}")

a=modeldata(model_name="gpt")
print(a)

print("\\ "*20)
'''"""
Create an ExperimentRun(BaseModel) for an ML training tracker with:

experiment_name: str (required, non-nullable)
parent_run_id: str | None (required key, can be None)
learning_rate: float = 0.001 (optional, non-nullable)
run_id: UUID (auto-generated fresh UUID per instance via default_factory)
metrics: dict[str, float] (defaults to a fresh empty dict {} via
default_factory)


Test creating 2 separate runs and verify run1.run_id != run2.run_id!
"""'''
from pydantic import BaseModel,Field
from uuid import UUID, uuid4

class Experimentrun(BaseModel):
    experiment_name: str
    parent_run_id: str | None
    learning_rate: float = 0.001
    run_id: UUID = Field(default_factory=uuid4)
    metrics: dict[str, float] = Field(default_factory=dict)


run1 = Experimentrun(experiment_name="model",parent_run_id=None)

run2 = Experimentrun(experiment_name="model",parent_run_id="RUN101")

print(run1)
print(run2)

print(run1.run_id != run2.run_id)
print("-"*30)
