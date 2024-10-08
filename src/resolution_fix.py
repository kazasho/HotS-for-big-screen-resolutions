import os
import sys
import re
from dotenv import load_dotenv

# Import user defined variables


load_dotenv()
Desired_resolution_w = os.getenv("Desired_resolution_w")
Desired_resolution_h = os.getenv("Desired_resolution_h")
MakeConfigReadOnly = os.getenv("MakeConfigReadOnly")
Log_level = os.getenv("Log_level")

# Initiate logging

from modules.Logger_factory import LoggerFactory

# Remove old log file if existing
if os.path.exists("resolution_fix.log"):
	os.remove("resolution_fix.log")

logger = LoggerFactory.get_logger("resolution_fix.log", log_level=Log_level)
logger.debug("Main: Logging setup complete")


# OS checker

from modules.OS_checker import OS_checker


HotS_config_path = OS_checker()

# Permission factory
from modules.File_permission_factory import File_read_only


Remove_read_only = File_read_only.Remove_read_only
Add_read_only = File_read_only.Add_read_only

# Change factory
from modules.Config_change_content import File_change_content

Change_content = File_change_content.Change_content

# Filecheck factory
# Check that config file exists, and if we can modify it


try:
	Remove_read_only(HotS_config_path, logger)
	with open(HotS_config_path, "r") as r:
		for count, line in enumerate(r):
			pass
		logger.info(f"Number of lines is: {count + 1}")
		if count + 1 <= 30:
			raise ValueError
	logger.info(f"{HotS_config_path} exists and is readable, continuing")
except FileNotFoundError:
	logger.error("Filecheck factory: Config file not found, launch game to have it created")
	print("Filecheck factory: Config file not found, launch game to have it created")
	sys.exit(0)
except ValueError:
	logger.error(f"Filecheck factory: File missing content, delete the file and launch the game to have a new one created. Path: {HotS_config_path}")
	print("Filecheck factory: File missing content, delete the file and launch the game to have a new one created. Path: ", HotS_config_path)
	sys.exit(0)
except:
	logger.error("Filecheck factory: Unknown exception raised")
	print("Filecheck factory: Unknown exception raised")

# Change factory
# Find current resolution


try:
	with open(HotS_config_path, 'r') as f:
		Width = re.findall(r'width=\d+', f.read())
	logger.info(f"Current width in config file: {Width[0]}")
except IndexError:
	# Create config line if missing
	logger.info("Width missing from config file, adding it")
	with open(HotS_config_path, 'a') as f:
		f.write('width=1920')
		Width = re.findall(r'width=\d+', f.read())
	logger.info(f"Current width in config file: {Width[0]}")

try:
	with open(HotS_config_path, 'r') as f:
		Height = re.findall(r'height=\d+', f.read())
	logger.info(f"Current height in config file: {Height[0]}")
except IndexError:
	# Create config line if missing
	logger.info("Height missing from config file, adding it")
	with open(HotS_config_path, 'a') as f:
		f.write('height=1200')
	with open(HotS_config_path, 'r') as f:
		Height = re.findall(r'height=\d+', f.read())
	logger.info(f"Current height in config file: {Height[0]}")

# Check if width and height is correct, fix it if wrong.
# Looks for the strings in the config file, and tries to change the values behind them based on user defined variables.
# If the strings are missing, they will be appended to the file
# Example: 1920 x 1200 results in height config element being missing due to being treated as standard. After changing to a different height and then back, then the application leaves height as a config element in the file


if Width[0] == "width=" + Desired_resolution_w:
	logger.info("Width is correct")
	print("Width is correct")
else:
	logger.info("Width wrong, fixing")
	print("Width wrong, fixing")
	Change_content(HotS_config_path, Width, Desired_resolution_w, logger)

if Height[0] == "height=" + Desired_resolution_h:
	logger.info("Height is correct")
	print("Height is correct")
else:
	logger.info("Height wrong, fixing")
	print("Height wrong, fixing")
	Change_content(HotS_config_path, Height, Desired_resolution_h, logger)

# Make config-file read only?


if MakeConfigReadOnly == "yes":
	Add_read_only(HotS_config_path, logger)
else:
	logger.info("MakeConfigReadOnly is either set to no, or wrong statement has been provided")
	print("MakeConfigReadOnly is either set to no, or wrong statement has been provided")
	sys.exit(0)