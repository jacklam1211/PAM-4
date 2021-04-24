import numpy as np
import matplotlib.pyplot as plt

#generate binary list
Number=123456789
NumberBinary="{0:b}".format(Number)
NumberBinaryA=[]
NumberBinaryA.extend(NumberBinary)
NumberBinaryA = list(map(int, NumberBinaryA))
if (len(NumberBinaryA)%2==1):
    NumberBinaryA.insert(0,0)
print(NumberBinaryA)
#Classify Levels
i=0
time=[]
ans=[]
while(i<len(NumberBinaryA)):
    if NumberBinaryA[i]==1 and NumberBinaryA[i+1]==0:
        ans.append(3)
    elif NumberBinaryA[i]==1 and NumberBinaryA[i+1]==1:
        ans.append(1)
    elif NumberBinaryA[i]==0 and NumberBinaryA[i+1]==1:
        ans.append(-1)
    elif NumberBinaryA[i]==0 and NumberBinaryA[i+1]==0:
        ans.append(-3)
    else:
        print("Error")
    i+=2

#Gen Graph
[time.append(i) for i in range(len(ans)+1)]
ans.insert(0,ans[0])
ax = plt.gca()
plt.step(time, ans)
plt.xlabel('Time')
plt.ylabel('Level')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.grid(1)
plt.show()