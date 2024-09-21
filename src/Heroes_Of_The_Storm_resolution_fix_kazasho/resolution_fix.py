import os
import stat
from stat import S_IREAD, S_IWUSR
import sys
import re
from modules.OS_checker import *

#User defined variables
Desired_resolution_w = "5120"
Desired_resolution_h = "1440"

#OS checker


HotS_config_path = OS_checker()

#Config factory


def Create_HotS_configfile():
	with open(HotS_config_path, "w") as file:
		file.write("accountCountry=NOR\n")
		file.write("ambientenvironmentmap=false\n")
		file.write("aolight=false\n")
		file.write("architecturePreference=2\n")
		file.write("chatpositionx=0.000000\n")
		file.write("chatpositiony=0.000000\n")
		file.write("creepnormalmap=true\n")
		file.write("creepQuality=1\n")
		file.write("creepselfshadow=false\n")
		file.write("creeptrans=true\n")
		file.write("creepUseGroundNormalTexture=false\n")
		file.write("deff=false\n")
		file.write("deffspec=false\n")
		file.write("deffspecpow=false\n")
		file.write("depthDisp=false\n")
		file.write("disableminimapsmartcommand=true\n")
		file.write("dof=false\n")
		file.write("extrapostprocessbuffer=false\n")
		file.write("fogvolume=false\n")
		file.write("foliagedensity=0.250000\n")
		file.write("foliagequality=1\n")
		file.write("GraphicsApi=Direct3D11\n")
		file.write("GraphicsOptionEffectsDetail=1\n")
		file.write("GraphicsOptionLightingQuality=0\n")
		file.write("GraphicsOptionModelQuality=2\n")
		file.write("GraphicsOptionMovies=0\n")
		file.write("GraphicsOptionOverallQualityVer7[21]=1\n")
		file.write("GraphicsOptionPhysicsQuality=1\n")
		file.write("GraphicsOptionPortraits=2\n")
		file.write("GraphicsOptionPostProcessing=1\n")
		file.write("GraphicsOptionReflections=0\n")
		file.write("GraphicsOptionShaderDetail=1\n")
		file.write("GraphicsOptionShadowQuality=1\n")
		file.write("GraphicsOptionSSAO=0\n")
		file.write("GraphicsOptionTerrainQuality=1\n")
		file.write("GraphicsOptionTextureQuality[2]=2\n")
		file.write("hdr8bit=true\n")
		file.write("height=" + Desired_resolution_h + "\n")
		file.write("highqualityframeblur=false\n")
		file.write("highqualityhaloblur=false\n")
		file.write("highqualityhaloblurgame=false\n")
		file.write("lastDeviceId=6088\n")
		file.write("lastReplaySaveMode=0\n")
		file.write("lightingLevel=2\n")
		file.write("lightmap=true\n")
		file.write("lightmapcastshadows=false\n")
		file.write("linearDepth=false\n")
		file.write("localao=false\n")
		file.write("localeidassets=enUS\n")
		file.write("localeiddata=enUS\n")
		file.write("localeidinstall=enUS\n")
		file.write("localight=false\n")
		file.write("localShadows=false\n")
		file.write("lowQualityMovies=true\n")
		file.write("MoviesSeen[1]=1\n")
		file.write("MusicHeard=1\n")
		file.write("normalzieHalfVector=false\n")
		file.write("OptionRevision=5\n")
		file.write("OptionRevisionAccount=0\n")
		file.write("parallax=false\n")
		file.write("particlelod=1\n")
		file.write("particleobjects=0.200000\n")
		file.write("particleterrain=0.500000\n")
		file.write("physicsClothEnabled=false\n")
		file.write("physicsdensity=160\n")
		file.write("physicsMaxComplexRagdolls=0\n")
		file.write("physicsRagdollsEnabled=false\n")
		file.write("ribbonlod=1\n")
		file.write("shadowmapsize=2048\n")
		file.write("showTimeStampInChat=true\n")
		file.write("soft=false\n")
		file.write("softshadows=false\n")
		file.write("SoundAutoDetectCPUCoreCount=16\n")
		file.write("soundchannels=64\n")
		file.write("soundglobal=true\n")
		file.write("SoundQuality=2\n")
		file.write("splatlod=1\n")
		file.write("ssparticles=false\n")
		file.write("targettexeldensity=1.400000\n")
		file.write("TerrainTextureLowResCacheSize=90\n")
		file.write("TerrainTextureSize=512\n")
		file.write("texQualityLevel=2\n")
		file.write("transparentshadows=false\n")
		file.write("treadlod=1\n")
		file.write("voicechatautojoinparty=false\n")
		file.write("voicechatinput={0.0.1.00000000}.{118ecc6d-6a26-4c73-aa4b-f899318eafd9}\n")
		file.write("voicechatjoinleavesound=false\n")
		file.write("voicechatothersjoinleavesound=false\n")
		file.write("voicechatremindjointeam=false\n")
		file.write("watercaustics=false\n")
		file.write("waterdeptheffects=false\n")
		file.write("waterflipbook=true\n")
		file.write("waterrendertargetformat=1\n")
		file.write("waterrendertargetsize=768\n")
		file.write("watershadow=false\n")
		file.write("width=" + Desired_resolution_w + "\n")
		file.write("winkeydisabled=true")
	print('Config factory: Created new config file sucessfully.')
	Permission_factory(Add_read_only)


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
		print("Change factory w: Could not find the 'width=' parameter in config file, re-creating config file")
		read_file.close()
		os.remove(HotS_config_path)
		Create_HotS_configfile()
		sys.exit()
	except:
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
		print("Change factory h: Could not find the 'height=' parameter in config file, re-creating config file")
		read_file.close()
		os.remove(HotS_config_path)
		Create_HotS_configfile()
		sys.exit()
	except:
		print("Change factory h: Error looping over config file")
		sys.exit()


#Filecheck factory
#Check that config file exists, and if we can modify it

try:
	Permission_factory(Remove_read_only)
	with open(HotS_config_path, "r") as r:
		for count, line in enumerate(r):
			pass
		print("Number of lines is: ", count + 1)
		if count + 1 <= 30:
			raise ValueError
	print(HotS_config_path + " exists and is readable, continuing.")
except FileNotFoundError:
	print("Filecheck factory: Config file not found, creating it.")
	Create_HotS_configfile()
	sys.exit()
except ValueError:
	print("Filecheck factory: File missing content, creating config file with medium graphics quality preset")
	os.remove(HotS_config_path)
	Create_HotS_configfile()
	sys.exit()
except:
	print("Filecheck factory: Exception raised")

#Change factory
#Find current resolution

with open(HotS_config_path, 'r') as f:
    Width = re.findall(r'width=\d+', f.read())
    
with open(HotS_config_path, 'r') as f:
    Height = re.findall(r'height=\d+', f.read())

print("Current width: " + Width[0])
print("Current height: " + Height[0])

#Check if width and height is correct, fix it if wrong


if Width[0] == "width=" + Desired_resolution_w:
	print("Width is correct, moving on.")
else:
	print("Width wrong, fixing.")
	Change_width()

if Height[0] == "height=" + Desired_resolution_h:
	print("Height is correct, moving on.")
else:
	print("Height wrong, fixing.")
	Change_height()

#Permission_factory(Add_read_only)