import csv 
import linecache
import pandas as pd 
line = linecache.getline("recc.csv",1)
line2 = linecache.getline("recc.csv",2)

# print((line))
# print((line2)) 
 
# with open("recc.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(" ".join(row))

 
# df = pd.read_csv('recc.csv',
#         sep='[:, |_]',
#         header=0,
#         usecols=["Option", "Name", "Price", "Description"],
#                 nrows=3)

# print(df)

# with open('recc.csv') as f:
#    csv_reader = csv.reader(f)
#    for index, row in enumerate(csv_reader):
#       if index == 1:
#          print("Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
#       elif index == 2:
#          print("Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
#       elif index == 3:
#          print("Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
       
#    print("Option D. Randomly select one for me! \nOption E. Leave blank (an average price of $`15000 will be used to calculate the final cost estimate)")
     

with open('recc.csv') as f:
   csv_reader = csv.reader(f)
   for index, row in enumerate(csv_reader):
      if index == 1 or index == 2 or index ==3:
         print("Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
print("Option D. Randomly select one for me! \nOption E. Leave blank (an average price of $`15000 will be used to calculate the final cost estimate)")
 

   
        