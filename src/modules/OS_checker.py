import os
import platform
import sys
from modules.Logger_factory import LoggerFactory


# A function checking which OS it is being executed on


def OS_checker(HotS_config_file, logger):
    OS = platform.system()
    global HotS_config_path
    if OS == 'Windows':
        logger.info("Detected OS: Windows")
        print("Detected OS: Windows")
        HotS_Document_Path = os.path.expanduser('~') + r"\Documents\Heroes of the Storm"
        HotS_config_path = HotS_Document_Path + "\\" + HotS_config_file
        return HotS_config_path
    elif OS == 'Darwin':
        logger.info("Detected OS: MacOS")
        print("Detected OS: MacOS")
        HotS_Document_Path = os.path.expanduser('~') + r"/Library/Application Support/Blizzard/Heroes of the Storm/"
        HotS_config_path = HotS_Document_Path + HotS_config_file
        return HotS_config_path
    else:
        logger.info(f"OS not supported, detected: {OS}")
        print("OS not supported, detected: ", OS)
        sys.exit(0)