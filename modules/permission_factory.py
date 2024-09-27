import os
import stat
from stat import S_IREAD, S_IWUSR

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