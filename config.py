import os,sys

LOAD_TIME_DELAY = 2

PAGE_URL = "https://thietbixonghoi.vn/may-xong-hoi-kho.html"

SAUNA_FOLDER = "https://www.maksauna.vn/wp-content/uploads/2024/07"

CURR_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

PRODUCT_FOLDER = "may-xong-kho"

PRODUCT_CAT = "may-xong-uot"

CSV_FOLDER = "CSV-Data"

IMG_FOLDER = "images"

product_cats = {
"SAWO": "may-xong-kho-sawo",
"EOS" : "may-xong-kho-eos",
"HARVIA" : "may-xong-kho-harvia",
"TYLO" : "may-xong-kho-tylo",
"HELO" : "may-xong-kho-helo",
"BOXER" : "may-xong-kho-boxer",
"AMEREC" : "may-xong-kho-amerec",
"FINNLEO" : "may-xong-kho-finnleo",
"SENTIOTEC" : "may-xong-kho-sentiotec",
}