# manual link 

import os
from tkinter import filedialog
from tkinter import *

# delimiter = input("type the delimeter you want: ")
delimiter = " "
outputfilename = input("type the output file name you want include it's extention ex)name.txt: ")
 
root = Tk()
root.dirName=filedialog.askdirectory()

Image_data_list = os.listdir(root.dirName)
Image_data_list.sort()

pardir = root.dirName.split("/")
img_dir_prefix = pardir[len(pardir)-1] + "\\"

print ("Image data directory :: "+root.dirName)

root = Tk()
root.dirName=filedialog.askdirectory()
 
Annotation_data_list = os.listdir(root.dirName)
Annotation_data_list.sort()

pardir = root.dirName.split("/")
anno_dir_prefix = pardir[len(pardir)-1] + "\\"

print ("Annotation data directory :: "+root.dirName)

root = Tk()
root.dirName=filedialog.askdirectory()
 
print ("Output directory :: "+root.dirName)



print("img count: " + str(len(Image_data_list)))
print("anno count: " + str(len(Annotation_data_list)))

if len(Image_data_list) != len(Annotation_data_list):
    print("Error Image and Annotation data should be 1 by 1 correspond, but now it's total number is different")

else:
    merged_List=[img_dir_prefix+i+delimiter+anno_dir_prefix+j for i,j in zip(Image_data_list,Annotation_data_list)] 

f = open(root.dirName+"/"+outputfilename,'w')

for item in merged_List:
    f.write(item+"\n")

f.close()
