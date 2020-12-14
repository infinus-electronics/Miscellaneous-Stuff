import os

path = os.path.realpath(__file__)

parent_path = path.rsplit("\\", 1)[0]

#print(parent_path)

files = os.listdir(parent_path)


#print(files)

for _file in files:
    if _file.split('.')[1] == 'jpg' or _file.split('.')[1] == 'jpeg':
        new_name = _file.replace(" ", "_")
        os.rename(parent_path+"\\"+_file, parent_path+"\\"+new_name)

