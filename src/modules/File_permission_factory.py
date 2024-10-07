# Permission factory
# Importable functions that can toggle the read-only attribute

import os
import stat
from stat import S_IREAD, S_IWUSR

class File_read_only(object):

#   Function to remove read-only attribute

    def Remove_read_only(config_path, logger):
        os.chmod(config_path, S_IWUSR|S_IREAD)
        logger.info("Permission factory: Removed read-only restriction")

#   Function to add read-only attribute

    def Add_read_only(config_path, logger):
        mode = os.stat(config_path).st_mode
        ro_mask = 0o777 ^ (stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH)
        os.chmod(config_path, mode & ro_mask)
        logger.info("Permission factory: Made file read-only")