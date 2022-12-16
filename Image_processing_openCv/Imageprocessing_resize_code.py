import cv2
import glob
files = glob.glob(r"Hand_Gun\\*")  # means that all pic include with jpg, png....etc
files = glob.glob(r"Hand_Gun\\*.jpeg") # means that only jpeg include pictures
# files = glob.glob("D:\\Eye_diseases\\test\\Cataracts\\*.jpeg")    is tra path ho ga  
#  end pr is ko extension b dkgh lni hai   jpg, jpeg, png
# /*.jpg   is ko end pr lazmi lgna hai otherwise error ay gga
#  ager path ka isseur hua pr b error ay
i = 0
for file in files:

    img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    
    print('Original Dimensions : ',img.shape)
    
    width = 100
    # height = img.shape[0] # keep original height
    height = 100
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    i +=1
    print('count numnber',i)
    print('Resized Dimensions  test: ',resized.shape)
    
    # cv2.imshow("Resized image", resized)
    cv2.imwrite(file,resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()