import cv2
import dlib
import imutils
from imutils import face_utils
import numpy as np
from scipy.ndimage import filters
from PIL import Image



face_detector = dlib.get_frontal_face_detector()
predict_points = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

img = cv2.imread('AMA_9169.JPG')
img = cv2.resize(img,(1280,720))

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray_image = cv2.blur(gray_image,(5,5))
pil_im = Image.fromarray(img) #usar
rects = face_detector(gray_image, 1)
x1=[]
y1=[]
w1=[]
h1=[]

cont = 0

for (i, rect) in enumerate(rects):
    reference_points= predict_points(gray_image, rect)
    reference_points = face_utils.shape_to_np(reference_points)
    
    # (x, y, w, h)
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    x1.append(x)
    y1.append(y)
    w1.append(w)
    h1.append(h)
    
    box = (x, y, (x+w),(y+h)) #usar
    region = pil_im.crop(box) #usar
    gauss_face = filters.gaussian_filter(region,10) #usar
    
    gauss_face = Image.fromarray(gauss_face) #usar
    
    pil_im.paste(gauss_face,box) #usar
    
    cont += 1  
    
    #pil_im = np.array(pil_im) #usar
    
    #cv2.rectangle(pil_im, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    
    
pil_im = np.array(pil_im) #usar

for i,n in enumerate(x1):
    cv2.rectangle(pil_im, (x1[i], y1[i]), (x1[i] + w1[i], y1[i] + h1[i]), (0, 150, 200), 2) 
    

cv2.putText(pil_im, "{} pessoas desfocadas".format(cont), (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 4)

#roi = img[first_point[1]:right_down[1],first_point[0]:right_down[0]]

cv2.imshow('_',pil_im)
cv2.waitKey()





