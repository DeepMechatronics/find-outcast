import csv
import tempfile
import time
from tempfile import NamedTemporaryFile
import glob
import os
import shutil
import ntpath
import pandas as pd

cwd = os.getcwd() 
print("Current working directory:")
print()  
name=""
input_name=""
for name in glob.glob(cwd+"/list_of_student.csv"):
    print(name)
for input_name in glob.glob(cwd+"/input.csv"):
    print(input_name)    
 
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
         if row[0].startswith('msm'):
             fw=row[0].split()[0]
             atl.append(fw)
             print(fw)
    print(atl)

with open(name, 'r') as file:
    reader = csv.reader(file)
         
    for row in reader:
         if row[0].startswith('msm'):
             fw=row[0].split()[0]
             atl.append(fw)
             print(fw)
    print(atl)    

df = pd.read_csv(input_name, usecols = [1])
print(df)            
li=[]

for column in df.columns:
     
    # Storing the rows of a column
    # into a temporary list
     li=df[column].tolist()
     
    # appending the temporary list
    
     
# Printing the final list
print(li)
print("print outcast")
outcast=set(atl)-set(li)
l_outcast=list(outcast)
with open('output.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(l_outcast)


