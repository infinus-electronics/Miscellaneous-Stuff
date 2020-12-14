import os

path = os.path.realpath(__file__)

parent_path = path.rsplit("\\", 1)[0]

#print(parent_path)

files = os.listdir(parent_path)

file_formats = []
for _file in files:
    if ('.'+_file.split('.')[1]) not in file_formats:
        file_formats.append("."+_file.split('.')[1])
print("File extensions found:")
print(file_formats)
instr = input("Select target file extensions with a comma seperated list(blank defaults to jpg and jpeg) \n")
instr = instr.replace(".", '') #remove occurences of blankspaces and dots
instr = instr.replace(" ", '')
#print(instr)


if len(instr) > 0: #user specified certain filenames
    file_extensions = instr.split(',')
else:
    file_extensions = ['jpg','jpeg']


#print(files)
rename_count = 0
for _file in files:
    if _file.split('.')[1] in file_extensions:
        rename_count = rename_count + 1

confirmation = input("Rename {0} files? (Y/N) \n".format(rename_count))

if confirmation == "y" or confirmation == "Y" or confirmation == "Yes" or confirmation == "yes":
    for _file in files:
       if _file.split('.')[1] in file_extensions:
            new_name = _file.replace(" ", "_")
            os.rename(parent_path+"\\"+_file, parent_path+"\\"+new_name)

