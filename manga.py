import cv2
import numpy as np

class Manga: 

    img = cv2.imread('/Users/hopeboxdesign/Desktop/TT.png')
   #导入图片 
   #import image

    img_grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
   #灰化图片 
   #turn the image into black and white 

    img_blur = cv2.blur(img_grey,(6,6))
   #把灰化的图片变模糊，防止边缘化的时候黑色色块过于密集复杂 
   #blur the image to prevent the black color blocks from being too dense and complex when bordering

    img_blurEdge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
   #将图片卡通化 
   #cartonize the image

    img_blurEdgeC = cv2.cvtColor(img_blurEdge, cv2.COLOR_GRAY2RGB)
   #把卡通化的图片格式调整为和原图的格式一致 
   #adjust the format of the cartonized image, so it can be consistent with the format of the original image
    
    img_overlap = cv2.addWeighted(img_blurEdgeC, 0.46, img, 0.53, 0)
   #将卡通化的图片与原图叠加，以上色 
   #overlap the cartonized image with the original image to make the cartonized image colorful
   
    cv2.imwrite('/Users/hopeboxdesign/Desktop/output.png', img_overlap)
   #成品导出 
   #export the product

