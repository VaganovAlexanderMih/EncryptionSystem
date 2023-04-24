import sys
import os

cur_path = os.getcwd()
cur_path += "/src"
sys.path.insert(1, cur_path)

print("Do you want to use graphic version of program or do you prefer command line?")
print("1 - graphic, 2 - command line")
version = int(input())

graphics_path = cur_path + "/main_graphics.py"
command_line_path = cur_path + "/main_command_line.py"

if (version == 1):
    exec(open(graphics_path).read())
elif (version == 2):
    exec(open(command_line_path).read())
else:
    print("Invalid argument. Aborting().")
    sys.exit()