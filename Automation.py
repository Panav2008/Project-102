import os
import shutil
source=input("Plese provide the Source path")
destination=input("plese provide the path for where you want to make a backup")
list_of_files=os.listdir(source)
for files in list_of_files:
    shutil.copy(source+"/"+files,destination+"/")