import csv
import tempfile
import time
from tempfile import NamedTemporaryFile
import glob
import os
import shutil
import ntpath

cwd = os.getcwd() 
print("Current working directory:")
print()  
name=""
for name in glob.glob(cwd+"/input/*.csv"):
    print(name)
roll_list=[ "MSM19B001","MSM19B002","MSM19B003","MSM19B004","MSM19B005","MSM19B006","MSM19B008","MSM19B009","MSM19B010","MSM19B011","MSM19B012","MSM19B013","MSM19B014",
"MSM19B015","MSM19B017","MSM19B018","MSM19B019","MSM19B020","MSM19B021","MSM19B023","MSM19B024","MSM19B025","MSM19B028","MSM19B030","MSM19B031","MSM19B032","MSM19B033",
"MSM19B034","MSM19B035","MSM19B036","MSM19B037","MSM19B038","MSM19B039","MSM19B040","MSM19B041","MSM19B042","MSM19B043","MSM19B044","MSM19B045","MSM19B046","MSM18B031"]
atl=[]
p_list=[]
a_list=[]
empty=[]
with open(name, 'r') as file:
    reader = csv.reader(file)
         
    for row in reader:
         if row[0].startswith('MSM'):
             fw=row[0].split()[0]
             atl.append(fw)
             print(fw)
          # if roll_list[2] == fw:
          # print(row)
             #if (fw in roll_list):
             time = row[2] 
             du=sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":"))) 
             if(du>3000*0.70):
              p_list.append(fw)
             else: 
              a_list.append(fw)
    print(atl)
    print("=============Present seperatiom=================")
    a_list=a_list+list(set(roll_list)-set(atl))
    print(p_list)
    print("=============Abbesnt seperatiom=================")
    print(a_list)

            

with open('main.csv', 'r') as file:
      reader_m = csv.reader(file)
     
      for row in reader_m:
           if row[2].startswith('MSM'):
              if row[2] in a_list:
                  print(row[2])
                  for i in range(len(row)):
                     if row[i] =='':
                        row[i]="A"
                        
                        break
                  print(row)
                  

              else:
                  for i in range(len(row)):
                     if row[i] =='':
                        row[i]="P"
                        
                        break
                  print(row)
           empty.append(row)         
print("=========================================")
print(empty)                  
with open('main.csv', 'w' , newline='') as file:
      writer_m = csv.writer(file)
      writer_m.writerows(empty)   
std=cwd+"/backup/"+ntpath.basename(name) 
shutil.move(name,std)                       


