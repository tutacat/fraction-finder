import math
#begin

min = ((3,1),math.pi-(3/1))
#min = ((22,7),math.pi-(22/7))
#min = ((355,113),math.pi-(355/113))
print(min)
for i in range(min[0][1],min[0][1]+1000,2):
    frac = ((round(math.pi*i),i),0)
    frac = (frac[0],math.pi - (frac[0][0]/frac[0][1]))
    if abs(frac[1]) < abs(min[1]):
        min = frac
        print(min)
