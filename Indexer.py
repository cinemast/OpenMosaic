import glob
import json
import cv2
import ntpath
import os

import features

DB_PATH = "./images"
INDEX_PATH = "./index/"
LENGTH = 50

def convertImage(path):
    image = cv2.imread(path)
    height, width, depth = image.shape
    ratio = float(height)/float(width)
    print (height, width, ratio)
    if height > width:
        image = cv2.resize(image, (LENGTH, int(LENGTH*ratio))) # width, height
        # image is now LENGTHpx width, now we crop it to the correct height
        h = int(LENGTH*ratio); # the final height
        margin = int(float(h-LENGTH)/float(2)) # margin to crop at top and bottom
        image = image[margin:(LENGTH + margin), 0:LENGTH] # crop image now
    else:
        image = cv2.resize(image, (int(LENGTH/ratio), LENGTH))
        # image is now LENGTHpx height, now we crop it to the correct width
        w = int(LENGTH/ratio); # final width
        margin = int(float(w-LENGTH)/float(2)) # calculate margin
        image = image[0:LENGTH, margin:(LENGTH+margin)] # crop image
    # finally store image
    cv2.imwrite(INDEX_PATH + ntpath.basename(path), image)
    return image

def getFileList():
    included_extenstions = ['jpg','bmp','png','gif' ] ;
    return [fn for fn in os.listdir(DB_PATH) if any([fn.endswith(ext) for ext in included_extenstions])];

def main():
    index = []
    if not os.path.exists(INDEX_PATH):
        os.makedirs(INDEX_PATH)
    files = glob.glob(DB_PATH + "/" + "*.jpg")
    
    entry = {}
    
    for file in files:
        print "Processing file: " + file
        image = convertImage(file)
        entry = features.extractFeature(image)
        entry["file"] = ntpath.basename(file)
        index.append(entry)

    with open(INDEX_PATH + "histogram.index", 'w') as outfile:
        json.dump(index, outfile, indent=4)
        
    print ("Index written to: " + INDEX_PATH + "histogram.index")

if __name__ == "__main__":
    main()