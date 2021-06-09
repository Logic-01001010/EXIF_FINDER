from PIL import Image

import os


directory = os.listdir('pictures')

print(directory)



for img in directory:


    print("\n\n===============================\n")

    print(img,'\n\n')
    
    image = Image.open("pictures/"+img)
    info = image._getexif();
    image.close()




    if type(info) == dict:

        try:
            print("● camera > " + info[271])
        except:
            print('# no camera')

        try:   
            print("● camera model > " + info[272])
        except:
            print('# no camera model')


        try:
            print("● GPS >", info[34853])
        except:
            print('# no GPS')



    else:
        print(img+' < no info')


    print("\n\n===============================\n\n")

# 271 카메라 (samsung)
# 272 카메라 모델 (SM-N976N)
# 34853 위치
# 
