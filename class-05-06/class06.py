#chan1 run only 1 block
if False:
    print ("True_block")
elif False:
    print ("True_block1")
elif True:
    print ("True_block2")
elif False:
    print ("True_block3")
else:
    print ("Else_block")
print ("pakistan")

from typing import Union

#grade : Union[int,float] = 7.0
#print (grade)

#per : Union[int,float] = 88
# per : | float =88
#grade : Union[ str, None ]

per : Union[int,float] =  int(input(" Enter your Percentage : \t "))
# per : | float =88
grade : Union [str, None] = None
if per >=80:
    grade = "A+"
elif per >=70:
    grade = "A"
elif per >=70:
    grade = "B"
elif per >=60:
    grade = "C"
elif per >=50:
    grade = "D"
elif per >=40:
    grade = "E"
elif per >=33:
    grade = "E"
else:
    grade = "F (fail)"
    
print(f"your Percentage is {per} your Grade is :\t {grade}")
