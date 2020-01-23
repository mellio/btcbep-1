import requests, sys, json, os, time, random
from bs4 import BeautifulSoup
from time import sleep
with open('cfg.json', 'r') as fh:
    json_str = fh.read()
    json_value = json.loads(json_str)
    sessid = json_value['sessid']

url = 'https://bitcoinbep.com/visit-friends'
urlc = 'https://bitcoinbep.com/captcha'
urlclaim = "https://bitcoinbep.com/friend.php?user_id=139177&t=1579697569&aid=1"
UA = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36"}
coke = {"PHPSESSID": sessid}

banner = f"""\033[1;35m
                                              
eeeee  eeeee e    e eeee eeeee       e  eeeee 
8   8  8   8 8    8 8    "   8       8  8   8 
8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 
88   8 88  8   88   88   88          88 88  8 
88   8 88  8   88   88ee 88ee8       88 88ee8 
                               eeeee
\033[1;36m=============================================
\033[1;32m ~ anthesphong1998@gmail.com (+6282195663814)
\033[1;36m=============================================          
"""

c = requests.Session()

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

os.system('python -m pip install requests bs4 -y')
os.system('clear')
print(banner)
sleep(2)

def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;32m» \033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining))
       sys.stdout.flush()
       sleep(1)

def username():
    r = c.post(url, cookies=coke, headers=UA)
    soup = BeautifulSoup(r.content, "html.parser")
    user = soup.find_all('span', class_="d-none d-sm-inline-block")
    for use in user:
        x = use.text
        if "Login" in x:
          print ("\r\033[1;31m» PHPSESSID Expired, Please sniff again!\n")
          sys.exit()
        else:
          mengetik(f"\033[1;35mTHIS SCRIPT IS NOT FOR SALE  \033[1;36m-  {x}\n\033[1;35mSCRIPT INI UNTUK NUYUL  \033[1;36m-  BitcoinBep.com\n")
        
def balance():
    r = c.post(url, cookies=coke, headers=UA)
    soup = BeautifulSoup(r.content, "html.parser")
    ball = soup.find('a', class_="font-size-lg")
    for bal in ball:
        x = ball.text
        sys.stdout.write(f"\r\033[1;32m» Your balance now {x}\n")
        
def claim():
    r = c.post(urlclaim, cookies=coke, headers=UA)
    response = requests.get(urlclaim)
    response.status_code
    if response:
        sys.stdout.write("\r\033[1;33m» Succes adding balance\n")
        
def captcha():
    r = c.post(url, cookies=coke, headers=UA)
    soup = BeautifulSoup(r.content, "html.parser")
    if soup.find("div",class_="g-recaptcha") :
        sys.stdout.write("\r\033[1;31m» Captcha detected\n")
        os.system(f'termux-open-url {urlc}')
        e = input("\r\033[1;32m» Press Enter to Continue")
        sleep(2)
    else:
        sleep(2)
        
sleep(2)
username()
sleep(1)
balance()
for i in range(5000000):
  sys.stdout.write("\r")
  sys.stdout.write("                                                              ")
  sys.stdout.write("\r")
  sys.stdout.write("\033[1;33m» Injecting...")
  sys.stdout.flush()
  claim()
  sleep(2)
  balance()
  sleep(2)
  captcha()
  tunggu(int(15))
