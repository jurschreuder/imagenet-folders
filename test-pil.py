import os
from glob import glob
from PIL import Image

inFolder = "lanczos"

folders = glob(inFolder + "/*/")
#print(folders)
for folder in folders:
    imgs = glob(folder + "*")
    for img in imgs:
        #print(img)
        try:
            Image.open(img)
        except ValueError as e:
            print(e)
            print(img)
            newPath = img + ".error"
            os.rename(img, newPath)
            print("renamed image to:", newPath)
