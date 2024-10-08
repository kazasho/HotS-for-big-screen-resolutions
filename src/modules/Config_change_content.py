import sys

class File_change_content:

    def Change_content(config_path, Current_content, Desired_change, logger):

        """
        A function that looks for a config element, and checks if it is set how we want it.
        Requires: A path to the config file, the current config (both config key and value),
        the desired change (only the value) and logger
        """

        logger.debug("Change_content started")

        Replaced_content = ""
        Separator = "="
        Config_key = Current_content[0].split(Separator, 1)[0] + Separator

        try:

            # Read the file

            read_file = open(config_path, "r")

            # Loop over file, searching for the content to replace

            for line in read_file:
                line = line.strip()
                New_content = line.replace(Current_content[0], Config_key + Desired_change)
                Replaced_content = Replaced_content + New_content + "\n"
            read_file.close()

            # Write replaced config to file

            with open(config_path, "w") as w:
                w.write(Replaced_content)

        except IndexError:

            logger.error(f"Change content: Could not find the {Config_key} parameter in config file, delete the file and launch the game to have it re-created. Path: {config_path}")
            print("Change content: Could not find the" + {Config_key} + "parameter in config file, delete the file and launch the game to have it re-created. Path: ", config_path)
            read_file.close()
            sys.exit(0)

        except:

            logger.error("Change content: Error looping over config file")
            print("Change content: Error looping over config file")
            sys.exit()

        logger.debug("Change_content: Function execution complete")