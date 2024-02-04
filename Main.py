import os
import shutil
S = "C:/Users/lenovo/OneDrive/Desktop/HomeWork/1st HW/Files"
D = "C:/Users/lenovo/OneDrive/Desktop/HomeWork/1st HW/MOVE Files"
List = os.listdir(S)
#print(List)
T = 0
for i in List:
    N,E=os.path.splitext(i)
    print(N)
    print(E)
    T = T + 1
    if E == " ":
       continue
    if E in [".txt",".dox"]:
        path1 = S+"/"+i
        path2 = D+"/"+"imagefile"
        path3 = D+"/"+"imagefile"+i
     #   print(path1)
      #  print(path3)
        if os.path.exists(path2):
            print("moving"," ",i)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"," ",i)
            shutil.move(path1,path3)

print("Total number of document :",T)
