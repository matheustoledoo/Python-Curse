import sys
import os
from PIL import Image

#grab the first and second argument
imageFolder = sys.argv[1]
outputFolder = sys.argv[2]


#check is new/ exist, if not created yet
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)


for filename in os.listdir(imageFolder):
    img = Image.open(f'{imageFolder}{filename}')
    cleanName = os.path.splitext(filename)[0]
    img.save(f'{outputFolder}{cleanName}.png', 'png')
    print('All done')

