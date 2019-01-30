import random
import os

num_var=7
num_clau=100
file = open("uf250-test7.cnf","w")
file.write("c This Formular is generated by mcnf\n")
file.write("c\n")
file.write("c    horn? no \n")
file.write("c    forced? no \n")
file.write("c    mixed sat? no \n")
file.write("c    clause length = 3 \n")
file.write("c\n")
file.write("p cnf "+str(num_var)+"  "+str(num_clau)+"\n")

map = {}
i=0
while(i<num_clau):
    a=random.randint(-num_var,num_var)
    b=random.randint(-num_var,num_var)
    c=random.randint(-num_var,num_var)
    if (abs(a)!=abs(b) & abs(a)!=abs(c) & abs(b)!=abs(c)):
        print(i)
        key=str(a)+str(b)+str(c);
        print(key)
        if key in map:
            continue
        if(a<0 & b<0 & c<0):
            continue
        file.write(str(a)+" "+str(b)+" "+ str(c)+" 0"+"\n")
        map[key]=1
        i+=1
    else :
        continue







