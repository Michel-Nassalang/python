import cv2
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--img", dest="imgfile", default=False, help ="le fichier image à lire")
arg.add_argument("-d", "--dest", dest="imgdest", help ="le fichier image à sauvegarder") 
args = arg.parse_args()
imgfile = args.imgfile
imgdest = args.imgdest

img=cv2.imread(imgfile)

if (imgdest):
	cv2.imwrite(imgdest,img)

cv2.imshow('image',img)
cv2.waitKey(0)

# python3 image.py -i charger_image.jpg -d image_enregistre.jpg