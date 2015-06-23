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
    image = cv2.resize(image, (LENGTH,LENGTH) )
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