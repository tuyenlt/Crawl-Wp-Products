import shutil
import os
import glob
from config import *
import pycurl

# def convert_png_to_jpg(input_path, output_path):
#     img_png = Image.open(input_path) 
#     img_png = img_png.convert('RGB')
# #The image object is used to save the image in jpg format 
#     img_png.save(output_path)

def download_image(url, save_as):
    with open(save_as, 'wb') as file:
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, file)
        curl.perform()
        curl.close()


def get_jpg_files(folder_path):
    # Ensure the folder path ends with a slash
    if not folder_path.endswith('/'):
        folder_path += '/'
    
    # Use glob to find all .jpg files in the folder
    jpg_files = glob.glob(f"{folder_path}*.jpg")
    
    # Extract just the file names from the full paths
    jpg_file_names = [os.path.basename(file) for file in jpg_files]
    
    return jpg_file_names

# Example usage
def moveImgsToUploadFolder():
    shutil.rmtree(IMG_FOLDER)
    os.makedirs(IMG_FOLDER)
    sub_folders = [name for name in os.listdir(PRODUCT_FOLDER) if os.path.isdir(os.path.join(PRODUCT_FOLDER, name))]
    for name in sub_folders:
        folder_path = PRODUCT_FOLDER + "/" + name + "/"
        print(folder_path)
        jpg_files = get_jpg_files(folder_path)
        for file in jpg_files : 
            source = folder_path + file
            target = f"images/{file[:-4]}.jpg"
            print(target)
            if not os.path.isfile(target + "/" + file): 
                shutil.copyfile(source,target)
