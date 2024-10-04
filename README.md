# Heroes of the Storm enable big screen resolutions

The script works on Windows and MacOS.
It must be run by the user account on the machine that will execute the game.

Works on Python v3.9.6

## First time setup

1. Make sure the package "python-dotenv" is installed (pip install python-dotenv). Working on building a installer that handles this automatically
2. Copy ".env.example" and make the new filename ".env"
3. Change the content of ".env" to you liking
4. Run "resolution_fix.py"

## When Blizzard.net launcher detects the script changes

After you have played the game or the battle.net client have scanned your files, a update button will appear instead of the "Play" button. After "Updating", the screen resolution will be reset.
Just run the script again when you have the "Play" button in the battle.net client, and then press "Play" to enjoy your full screen resolution in the game yet again :)