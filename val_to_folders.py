from shutil import copyfile
import re
import os

inFolder = "lanczos"
outFolder = "folders"

# name: ILSVRC2012_val_00031255.png
def createName(i):
    name = "ILSVRC2012_val_000"
    if i < 10000:
        name += "0"
    if i < 1000:
        name += "0"
    if i < 100:
        name += "0"
    if i < 10:
        name += "0"
    name += str(i)
    name += ".png"
    return name

# getFolderNames creates folders for all labels and returns a map linking labels to folders
def getFolderNames(outFolder):
    folders = [""]*1001 # 0 is not used
    with open("map_clsloc.txt") as f:
        for line in f:
            print(line)
            tok = line.split()
            folders[int(tok[1])] = tok[0]
            os.makedirs(outFolder + "/"+tok[0])
    return folders



# process all images

folders = getFolderNames(outFolder)

with open("ILSVRC2012_validation_ground_truth.txt") as f:
    for i, line in enumerate(f):
        inPath = inFolder + "/" + createName(i+1)
        outPath = outFolder + "/" + folders[int(line)] + "/" + createName(i)

        copyfile(inPath, outPath)
