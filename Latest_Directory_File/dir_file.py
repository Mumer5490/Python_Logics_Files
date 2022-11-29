import glob
import os

# code one

list_of_files = glob.glob('images\\*.png') #
#  * is ka means hai k all images aayy wo .png , .jpg or koi b ho skti hai etc
# .png is ka matlab hai k sirf .png ki latest img ayy
# images ya folder ka name hai 
# yaha pr images ka name nai likhna

list_of_files = glob.glob('images\\*') # 
# images ya folder ka name hai
# * is ka matlab hai khh all imges ayy like .jpg, .png etc
# imp note .png , .jpg nai likhna

latest_file = max(list_of_files, key=os.path.getctime)
print (latest_file)


# code two
folder_path = r"images"
file_type = r'\\*'
files = glob.glob(folder_path+file_type)
max_file = max(files, key=os.path.getctime)
print(max_file)

