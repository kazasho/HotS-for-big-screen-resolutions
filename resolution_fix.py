import os
import stat
from stat import S_IREAD, S_IWUSR
import sys
import re
from modules.OS_checker import *
import logging
from dotenv import load_dotenv

#Import user defined variables


load_dotenv()
Desired_resolution_w = os.getenv("Desired_resolution_w")
Desired_resolution_h = os.getenv("Desired_resolution_h")
MakeConfigReadOnly = os.getenv("MakeConfigReadOnly")

# Configure basic logging
logging.basicConfig(filename='resolution_fix.log', level=logging.INFO, format='%(asctime)s %(message)s')


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
	logging.debug("Permission factory: Fixing read-only attributte")
	func()
	if func == Add_read_only:
		logging.info("Permission factory: Made file read-only")
	elif func == Remove_read_only:
		logging.info("Permission factory: Removed read-only restriction")
	else:
		logging.error("Permission factory: Wrong or missing parameter parsed")
		print("Permission factory: Wrong or missing parameter parsed")


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
		logging.error(f"Change factory w: Could not find the 'width=' parameter in config file, delete the file and launch the game to have it re-created. Path: {HotS_config_path}")
		print("Change factory w: Could not find the 'width=' parameter in config file, delete the file and launch the game to have it re-created. Path: ", HotS_config_path)
		read_file.close()
		sys.exit(0)
	except:
		logging.error("Change factory w: Error looping over config file")
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
		logging.error(f"Change factory h: Could not find the 'height=' parameter in config file, delete the file and launch the game to have it re-created. Path: {HotS_config_path}")
		print("Change factory h: Could not find the 'height=' parameter in config file, delete the file and launch the game to have it re-created. Path: ", HotS_config_path)
		read_file.close()
		sys.exit(0)
	except:
		logging.error("Change factory h: Error looping over config file")
		print("Change factory h: Error looping over config file")
		sys.exit()


#Filecheck factory
#Check that config file exists, and if we can modify it


try:
	Permission_factory(Remove_read_only)
	with open(HotS_config_path, "r") as r:
		for count, line in enumerate(r):
			pass
		logging.info(f"Number of lines is: {count + 1}")
		if count + 1 <= 30:
			raise ValueError
	logging.info(f"{HotS_config_path} exists and is readable, continuing")
except FileNotFoundError:
	logging.error("Filecheck factory: Config file not found, launch game to have it created")
	print("Filecheck factory: Config file not found, launch game to have it created")
	sys.exit(0)
except ValueError:
	logging.error(f"Filecheck factory: File missing content, delete the file and launch the game to have a new one created. Path: {HotS_config_path}")
	print("Filecheck factory: File missing content, delete the file and launch the game to have a new one created. Path: ", HotS_config_path)
	sys.exit(0)
except:
	logging.error("Filecheck factory: Unknown exception raised")
	print("Filecheck factory: Unknown exception raised")

#Change factory
#Find current resolution


try:
	with open(HotS_config_path, 'r') as f:
		Width = re.findall(r'width=\d+', f.read())
	logging.info(f"Current width in config file: {Width[0]}")
	#print("Current width in config file: " + Width[0])
except IndexError:
	# Create config line if missing
	logging.info("Width missing from config file, adding it")
	with open(HotS_config_path, 'a') as f:
		f.write('width=1920')
		Width = re.findall(r'width=\d+', f.read())
	logging.info(f"Current width in config file: {Width[0]}")
	#print("Current width in config file: " + Width[0])
try:
	with open(HotS_config_path, 'r') as f:
		Height = re.findall(r'height=\d+', f.read())
	logging.info(f"Current height in config file: {Height[0]}")
	#print("Current height in config file: " + Height[0])
except IndexError:
	# Create config line if missing
	logging.info("Height missing from config file, adding it")
	with open(HotS_config_path, 'a') as f:
		f.write('height=1200')
	with open(HotS_config_path, 'r') as f:
		Height = re.findall(r'height=\d+', f.read())
	logging.info(f"Current height in config file: {Height[0]}")
	#print("Current height in config file: " + Height[0])

# Check if width and height is correct, fix it if wrong.
# Looks for the strings in the config file, and tries to change the values behind them based on user defined variables.
# If the strings are missing, they will be appended to the file
# Example: 1920 x 1200 results in height config element being missing due to being treated as standard. After changing to a different height and then back, then the application leaves height as a config element in the file


if Width[0] == "width=" + Desired_resolution_w:
	logging.info("Width is correct")
	print("Width is correct")
else:
	logging.info("Width wrong, fixing")
	print("Width wrong, fixing")
	Change_width()

if Height[0] == "height=" + Desired_resolution_h:
	logging.info("Height is correct")
	print("Height is correct")
else:
	logging.info("Height wrong, fixing")
	print("Height wrong, fixing")
	Change_height()

# Make config-file read only?


if MakeConfigReadOnly == "yes":
	logging.info("Making config file read-only")
	Permission_factory(Add_read_only)
else:
	logging.info("MakeConfigReadOnly is either set to no, or wrong statement has been provided")
	print("MakeConfigReadOnly is either set to no, or wrong statement has been provided")
	sys.exit(0)