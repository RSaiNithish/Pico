import os
from PIL import Image



def  compress(file, c_path, path):
    os.chdir(path)
    filepath = os.path.join(os.getcwd(), file)
    picture = Image.open(filepath)
    os.chdir(c_path)
    picture.save(file,"JPEG",optimize=True,quality=80)

    

def main():
    print("in")
    path = os.getcwd()
    c_path = "E:\Python3 For MM\pico test"
    os.chdir(path)
    print(c_path)
    for folders,folderNames,file in os.walk(os.getcwd()):       
        for K in file:
            if K.endswith('.jpg') or K.endswith('.JPG'):
                print(K)
                compress(K,c_path,path)
                
        

                    
if __name__=="__main__":
    main()
