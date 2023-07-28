import requests
import random
import string
import threading
from bs4 import BeautifulSoup

password = input("Nhập Pass: ")
dem = 0

lock = threading.Lock()

def huydev_user(user, mail, pas):
    global dem
    headers = {
        "Host": "trieuphuc.dev",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Origin": "https://trieuphuc.dev",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://trieuphuc.dev/reg",
        "Cookie": "PHPSESSID=2ff2684104a6e5a3cdd2d1df7a659fe4",
    }

    data = {
        "email": mail,
        "pass": pas
    }
    
    response = requests.post("https://trieuphuc.dev/ajax/nguoidung/dangky.php", data=data, headers=headers).text
    
    with lock:
        dem += 1
        print("•Số acc đã tạo:", dem)
        print(response)
    

def huydev():
    i = 1000
    while True:
        if threading.active_count() - 1 < 10:
            i += 1
            random_chars = random.choices(string.ascii_letters + string.digits, k=10)
            user = f"{''.join(random_chars)}"
            mail = f"{user}@gmail.com"
            pas = password
            threading.Thread(target=huydev_user, args=(user, mail, pas)).start()

huydev()
