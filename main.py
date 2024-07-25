from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
from config import *
from unidecode import unidecode
from imgsHandle import download_image, moveImgsToUploadFolder
from CsvConvert import convertToCSV

LOAD_TIME_DELAY = 2




def format_cat(cat = ""):
    cat = unidecode(cat)
    cat = cat.lower()
    cat = cat.replace(" ", "-")
    return cat


class CrawSession:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('disable-notifications')
        chrome_options.add_argument("--start-maximized");
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
        self.product_link = []
        if not os.path.exists(PRODUCT_FOLDER):
            os.makedirs(PRODUCT_FOLDER)
        
        
    def create_product_link(self): 
        self.driver.get(PAGE_URL)
        self.cats = []
        cats_eles = self.driver.find_elements(By.CSS_SELECTOR, ".prod-tab.clearfix")
        for cat in cats_eles:
            self.cats.append(cat.find_element(By.TAG_NAME, "a").text)
        for cat in self.cats:
            print(format_cat(cat))
        sleep(1)
        product_eles = self.driver.find_elements(By.CLASS_NAME,"profeatured-img")
        print(product_eles.__len__())
        for ele in product_eles: 
            link_ele = ele.find_element(By.TAG_NAME, "a")
            link = link_ele.get_attribute("href")
            name = link_ele.find_element(By.TAG_NAME, "img").get_attribute("alt")
            name = name.replace("/","-")
            cat = ""
            for c in self.cats:
                # print(name.upper())
                tmp = c.replace("MÁY XÔNG KHÔ ","")
                if tmp in name.upper():
                    cat = c
                    break
            cat = format_cat(cat)
            self.product_link.append({ "name" : name , 
                                      "cat" : cat,
                                    "val" : link})
            img_dir = PRODUCT_FOLDER + "/" + name
            if not os.path.exists(img_dir):
                os.makedirs(img_dir)
                
        old_link = []
        # if os.path.exists(f"{PRODUCT_FOLDER}/product_link.txt"):
        #     with open(f"{PRODUCT_FOLDER}/product_link.txt",mode="r",encoding="utf-8") as file:
        #         for line in file.readlines():
        #             print(f"old - link {line}")
        #             old_link.append(line)
        #         file.close()
                
        # with open(f"{PRODUCT_FOLDER}/product_link.txt",mode="a",encoding="utf-8") as file:
        #     for link in self.product_link:
        #         if link["val"] + "\n" not in old_link:
        #             print(f"add link - {link["val"]}")
        #             print(f"cat - {link["cat"]}")
        #             file.write(link["val"] + "\n")
        #     file.close        
            
            
            
    def get_image(self):
        for link in self.product_link:
            print(link["name"])
            print(link["val"])
            self.driver.get(link["val"])
            sleep(0.5)
            self.get_des(link["name"])
            tmp = self.driver.find_element(By.CLASS_NAME, "product-detail-image")
            product_image_ele = tmp.find_elements(By.CLASS_NAME, "owl-item")
            img_list = []
            for ele in product_image_ele:
                ele = ele.find_element(By.TAG_NAME,"img")
                img_path = ele.get_attribute('src')
                print(img_path)
                img_list.append(img_path)
            id = 1
            for img in img_list:
                img_path = PRODUCT_FOLDER + "/" + link["name"] + "/" + link["name"]+ "-" + str(id) + ".jpg"
                download_image(img,img_path)
                id = id + 1
                
    # def get_text(self):

            
    def save_des(self):
        for link in self.product_link:
            self.driver.get(link["val"])
            self.get_des(link["name"])                
            
    def get_des(self,product_name):
        tab = self.driver.find_element(By.CLASS_NAME,"product-summary")                
        text = tab.get_attribute("innerText")
        des_path =  PRODUCT_FOLDER + "/" + product_name  + "/" + product_name + ".txt"
        with open(des_path,mode= "w",encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    ss = CrawSession()
    ss.create_product_link()
    ss.get_image()
    moveImgsToUploadFolder()
    convertToCSV()