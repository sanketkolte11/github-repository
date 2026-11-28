from pydantic import BaseModel,Field,ValidationError
from decimal import Decimal
 
class tranningmodel(BaseModel):
    id : int = Field(gt=0 , le = 1000)
    batch_size : int = Field(gt=0 ,multiple_of=8)
    lerning_rate : float = Field(gt=0.0 , le=1.0 ,allow_inf_nan=False)
    budget : Decimal = Field(gt= 0,max_digits=8,decimal_places=2)

#valid senario
a=tranningmodel(id=12,batch_size=32,lerning_rate=0.8,budget=12.20)
print(a)

print("^"*20)
#invalid senario
try:
    tranningmodel(id=1200,batch_size=15,lerning_rate=9.2,budget=12.20)
except ValidationError as e:
    print(f"number or errror found in case : {e.error_count()}")
    for i in e.errors():
        print(f" field :{i['loc']} , masg : {i['msg']}")


'''it will give an errror beacause the value fail while validating'''
print("-"*20)

#String constrain 

from typing import Annotated
from pydantic import BaseModel,ValidationError,Field,StringConstraints

cleanstring = Annotated[str , StringConstraints(strip_whitespace=True, min_length=2, to_upper=True)]
checkrollno = Annotated[str , StringConstraints(strip_whitespace=True , to_upper=True , pattern="^[A-Za-z]{2,5}-\d{3}$")]
'''^ symbol start ,[A-za-z] capital and small abcd,{2,5}length of abcd ,-\d mean digit ,{3} for 3 digit length , $ for end the expression'''

class prac(BaseModel):
    name : cleanstring
    roll_no : checkrollno

#valid senario

b = prac(name=" ram ",roll_no="asdb-234")
print(b)
print(">"*20)
#valid using regex(regular experssion)
b1 = prac(name=" Shamm   ",roll_no="abc-123")
print(b1)
print("<"*20)
#inavalid senario 
try:
    prac(name=" K",roll_no="abcds-21312")
except ValidationError as e:
    print(f"find the number of error in case : {e.error_count()}")
    for i in e.errors():
        print(f"field : {i['loc']}, masg : {i['msg']}")


# print(">-<"*20)

# print("> <"*20)

# print("| |"*20)

# print("? ?"*20)

# print("~ "*20)

# print("*  *"*20)
