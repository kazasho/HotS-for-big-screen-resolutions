import sys

class File_change_content:

    def Change_content(config_path, Current_content, Desired_change, Separator, logger):

        """
        A function that looks for a config element, and checks if it is set how we want it.
        
        Requires: A path to the config file, the current config (both config key and value),
        the desired change (only the value) and logging object
        """

        logger.debug("Change content started")

        Replaced_content = ""
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

            logger.info(f"Change content: Config element set to {Config_key}{Desired_change}")

        except IndexError:

            logger.error(f"Change content: Could not find the {Config_key} parameter in config file, delete the file and launch the game to have it re-created. Path: {config_path}")
            print("Change content: Could not find the" + {Config_key} + "parameter in config file, delete the file and launch the game to have it re-created. Path: ", config_path)
            read_file.close()
            sys.exit(0)

        except:

            logger.error("Change content: Error looping over config file")
            print("Change content: Error looping over config file")
            sys.exit()

        logger.debug("Change content: Function execution complete")


    def File_check_factory(Remove_read_only, config_path, logger):

        """
        Does file exist and contain data?
        
        Requires: Remove_read_only, path to the config file and logging object
        """

        try:
            Remove_read_only(config_path, logger)
            with open(config_path, "r") as r:
                for count, line in enumerate(r):
                    pass
                logger.info(f"Number of lines is: {count + 1}")
                if count + 1 <= 30:
                    raise ValueError
            logger.debug(f"{config_path} exists and is readable, continuing")

        except FileNotFoundError:
            logger.error("Filecheck factory: Config file not found, launch game to have it created")
            print("Filecheck factory: Config file not found, launch game to have it created")
            sys.exit(0)

        except ValueError:
            logger.error(f"Filecheck factory: File missing content, delete the file and launch the game to have a new one created. Path: {config_path}")
            print("Filecheck factory: File missing content, delete the file and launch the game to have a new one created. Path: ", config_path)
            sys.exit(0)

        except:
            logger.error("Filecheck factory: Unknown exception raised")
            print("Filecheck factory: Unknown exception raised")