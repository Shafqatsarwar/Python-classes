from typing import List
#index            0      1       2       3         4        5
fruits:List =['banana','apple','peach','banana1','appl2','peach3']
# index        -6        -5       -4      -3      -2        -1
for i in range(len(fruits)-1,0,-1):
    print (fruits[i])

print('-------\n')