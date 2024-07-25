import os
from unidecode import unidecode
from config import *
from imgsHandle import get_jpg_files

folder = PRODUCT_FOLDER

def get_cat_from_name(name = ""):
    keys = product_cats.keys()
    for key in keys:
        if key in name.upper():
            print(key)
            return product_cats[key]
    return "none"

def convertToCSV():
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

    product_list = []

    for name in sub_folders:
        des = ""
        with open(f"./{PRODUCT_FOLDER}/{name}/{name}.txt",
                mode='r',
                encoding="utf-8") as f: 
            des = f.read()
        cat = get_cat_from_name(name)
        imgs = get_jpg_files(f"./{PRODUCT_FOLDER}/{name}/")
        images = []
        main_img = f"{SAUNA_FOLDER}/{name}-1.jpg"
        for img in imgs:
            img = f"{SAUNA_FOLDER}/{img[:-4]}.jpg" 
            img = unidecode(img)
            img = img.replace(" ","-")
            images.append(img)
        
        
        product = {
            "name" : name,
            "main_img": main_img,
            "images" : images,
            "description" : des,
            "cat" : cat,
        }
        
        product_list.append(product)
        
    fields = ['name', 'main_img', 'images', 'description', "cat"]
    if not os.path.exists(CSV_FOLDER):
        os.makedirs(CSV_FOLDER)
    filename = f"{CSV_FOLDER}/{PRODUCT_CAT}.csv"

    # writing to csv file
    with open(filename, mode='w',encoding="utf-8") as csvfile:
        # creating a csv dict writer object
        csvfile.write("\"name\",\"main_img\",\"images\",\"description\",\"cat\"\n")
        for product in product_list:
            csvfile.write("\""+ product["name"] + "\",\"" + product["main_img"] + "\",\"")
            for img in product["images"]:
                csvfile.write(img)
                if img != product["images"][-1]:
                    csvfile.write(" | ")
            csvfile.write("\",\"" + product["description"] + "\",\"" + product["cat"] + "\"\n")

