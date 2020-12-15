import sys

from tempfile import mkstemp
from shutil import copymode, move
from os import fdopen, remove

try:
    old_file_path = sys.argv[1]
except IndexError:
    old_file_path = input('Specify Target Path\n')

found_body = False
file_handler, new_file_path = mkstemp()
with fdopen(file_handler, 'w', encoding="utf-8") as new_file:
    with open(old_file_path, encoding="utf-8") as old_file:
        for line in old_file:
            # debug note: use print(repr()) to show newline characters
            if line == "body {\n":
                found_body = True
                print('found a body')
            
            if "font-family: var(--jp-ui-font-family);" in line and found_body == True:
                new_file.write(line.replace('font-family: var(--jp-ui-font-family);', '/*font-family: var(--jp-ui-font-family);*/'))
                found_body = False
                continue

            new_file.write(line)

copymode(old_file_path, new_file_path) #copy permissions
remove(old_file_path)
move(new_file_path, old_file_path)
