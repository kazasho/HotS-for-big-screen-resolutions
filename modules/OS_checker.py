import os
import platform
import sys
import logging

HotS_config_file = "Variables.txt"

def OS_checker():
    OS = platform.system()
    global HotS_config_path
    if OS == 'Windows':
        logging.info("Detected OS: Windows")
        print("Detected OS: Windows")
        HotS_Document_Path = os.path.expanduser('~') + r"\Documents\Heroes of the Storm"
        HotS_config_path = HotS_Document_Path + "\\" + HotS_config_file
        return HotS_config_path
    elif OS == 'Darwin':
        logging.info("Detected OS: MacOS")
        print("Detected OS: MacOS")
        HotS_Document_Path = os.path.expanduser('~') + r"/Library/Application Support/Blizzard/Heroes of the Storm/"
        HotS_config_path = HotS_Document_Path + HotS_config_file
        return HotS_config_path
    else:
        logging.info(f"OS not supported, detected: {OS}")
        print("OS not supported, detected: ", OS)
        sys.exit(0)