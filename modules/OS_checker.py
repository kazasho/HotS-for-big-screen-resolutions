import os
import platform
import sys

HotS_config_file = "Variables.txt"

def OS_checker():
    OS = platform.system()
    global HotS_config_path
    if OS == 'Windows':
        print("Detected OS: Windows")
        HotS_Document_Path = os.path.expanduser('~') + r"\Documents\Heroes of the Storm"
        HotS_config_path = HotS_Document_Path + "\\" + HotS_config_file
        return HotS_config_path
    elif OS == 'Darwin':
        print("Detected OS: Macos")
        HotS_Document_Path = os.path.expanduser('~') + r"/Library/Application Support/Blizzard/Heroes of the Storm/"
        HotS_config_path = HotS_Document_Path + HotS_config_file
        return HotS_config_path
    else:
        print("OS not supported, detected: ", OS)
        sys.exit(0)