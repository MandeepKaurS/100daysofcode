i=0;
name=[]
age=[]
while(i<3): #Taking Inputs
  name.append(input("Comment vous vous applez?"))
  age.append(input("Quel age avez vous?"))
  i+=1
  #Data Types
  #print(type(age)) TYPE checking
location=0
for j in range(0,2):
  max=age[j]
  if(age[j+1]>max):
    max=age[j+1]
    location=j+1
print(name[location],"is the eldest and is ",age[location]," years old")

  
  