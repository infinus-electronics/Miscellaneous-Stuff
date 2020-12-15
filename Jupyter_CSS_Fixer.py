import sys

from tempfile import mksfile, mkstemp
from shutil import copymode, mode, move
from os import fdopen, remove

old_file_path = sys.argv[1]


found_body = False
file_handler, new_file_path = mkstemp()
with fdopen(file_handler, 'w') as new_file:
    with open(old_file) as old_file:
        for line in old_file:

            if line == "body{":
                found_body = True
            
            if "font-family: var(--jp-ui-font-family);" in line and flag == True:
                new_file.write(line.replace('font-family: var(--jp-ui-font-family);', '/*font-family: var(--jp-ui-font-family);*/'))
                found_body = False
                continue

            new_file.write(line)

copymode(old_file_path, new_file_path) #copy permissions
remove(old_file_path)
move(new_file_path, old_file_path)
