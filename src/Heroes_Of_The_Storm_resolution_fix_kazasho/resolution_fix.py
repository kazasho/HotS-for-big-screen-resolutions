import os
import stat
from stat import S_IREAD, S_IWUSR
import sys
import re
from modules.OS_checker import *

#User defined variables


Desired_resolution_w = "5120"
Desired_resolution_h = "1440"

#OS checker


HotS_config_path = OS_checker()

#Permission factory


def Remove_read_only():
	os.chmod(HotS_config_path, S_IWUSR|S_IREAD)


def Add_read_only():
	mode = os.stat(HotS_config_path).st_mode
	ro_mask = 0o777 ^ (stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH)
	os.chmod(HotS_config_path, mode & ro_mask)

def Permission_factory(func):
    print("Permission factory: Fixing read-only attributte.")
    func()
    if func == Add_read_only:
        print("Permission factory: Made file read-only.")
    elif func == Remove_read_only:
        print("Permission factory: Removed read-only restriction.")
    else:
        print("Permission factory: Wrong or missing parameter parsed.")


#Change factory

def Change_width():
	Replaced_width = ""
	try:
		read_file = open(HotS_config_path, "r")
		for line in read_file:
			line = line.strip()
			New_width = line.replace(Width[0], "width=" + Desired_resolution_w)
			Replaced_width = Replaced_width + New_width + "\n"
		read_file.close()
		with open(HotS_config_path, "w") as w:
			w.write(Replaced_width)
	except IndexError:
		print("Change factory w: Could not find the 'width=' parameter in config file, delete the file and launch the game to have it re-created. Path: ", HotS_config_path)
		read_file.close()
		sys.exit(0)
	except:
		print("Change factory w: Error looping over config file")
		sys.exit()

def Change_height():
	Replaced_height = ""
	try:
		read_file = open(HotS_config_path, "r")
		for line in read_file:
			line = line.strip()
			New_height = line.replace(Height[0], "height=" + Desired_resolution_h)
			Replaced_height = Replaced_height + New_height + "\n"
		read_file.close()
		with open(HotS_config_path, "w") as w:
			w.write(Replaced_height)
	except IndexError:
		print("Change factory h: Could not find the 'height=' parameter in config file, delete the file and launch the game to have it re-created. Path: ", HotS_config_path)
		read_file.close()
		sys.exit(0)
	except:
		print("Change factory h: Error looping over config file")
		sys.exit()


#Filecheck factory
#Check that config file exists, and if we can modify it


try:
	Permission_factory(Remove_read_only)
	with open(HotS_config_path, "r") as r:
		for count, line in enumerate(r):
			pass
		print("Number of lines is: ", count + 1)
		if count + 1 <= 30:
			raise ValueError
	print(HotS_config_path + " exists and is readable, continuing.")
except FileNotFoundError:
	print("Filecheck factory: Config file not found, launch game to have it created.")
	sys.exit(0)
except ValueError:
	print("Filecheck factory: File missing content, delete the file and launch the game to have a new one created. Path: ", HotS_config_path)
	sys.exit(0)
except:
	print("Filecheck factory: Exception raised")

#Change factory
#Find current resolution


with open(HotS_config_path, 'r') as f:
    Width = re.findall(r'width=\d+', f.read())
    
with open(HotS_config_path, 'r') as f:
    Height = re.findall(r'height=\d+', f.read())

print("Current width: " + Width[0])
print("Current height: " + Height[0])

#Check if width and height is correct, fix it if wrong


if Width[0] == "width=" + Desired_resolution_w:
	print("Width is correct, moving on.")
else:
	print("Width wrong, fixing.")
	Change_width()

if Height[0] == "height=" + Desired_resolution_h:
	print("Height is correct, moving on.")
else:
	print("Height wrong, fixing.")
	Change_height()

#Permission_factory(Add_read_only)