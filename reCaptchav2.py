import speech_recognition as sr
import time,requests,pydub,subprocess,os,random,pyautogui
from seleniumwire import webdriver
from seleniumwire.webdriver.common.action_chains import ActionChains
from seleniumwire.webdriver.common.by import By
from seleniumwire.webdriver.support.ui import WebDriverWait
from seleniumwire.webdriver.support import expected_conditions as EC
from seleniumwire.webdriver.common.keys import Keys

def convert_to_wav(name):
    r=sr.Recognizer()
    with sr.AudioFile(name) as source:
        return r.recognize_google(r.listen(source))

def create_file(url):
    file = open(f'audio{random.randint(0,100)}.mp3', 'wb')
    file.write(requests.get(url=url).content)
    file.close()
    name=f'{file.name[:-3]}wav'
    subprocess.call(['ffmpeg', '-i', file.name, name])
    os.remove(file.name)
    return convert_to_wav(name)

def audio():
    download=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,'rc-audiochallenge-tdownload-link')))
    field=browser.find_element_by_id('audio-response')
    ActionChains(browser).move_to_element(field).perform()
    field.send_keys(create_file(download.get_attribute('href')))
    verify=browser.find_element_by_id('recaptcha-verify-button')
    ActionChains(browser).move_to_element(verify).perform()
    verify.click()
    try:
        browser.find_element_by_id('audio-response')
        time.sleep(2)
        audio()
    except: pass

browser=webdriver.Chrome('C:\\Users\\Admin\\PycharmProjects\\pych\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe')
browser.header_overrides={  #general header parameters that bypass reCAPTCHAv2
'authority': 'www.google.com',
'method': 'GET',
'path': '/recaptcha/api2/demo',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
'cookie': 'ANID=AHWqTUkQ9iV0ANRbie55Fi4YFFUVJ832LHDVU9PS2P34WVB6Y2BGUOs73Z2Y9Knd; SID=wQf5nBIQHQgbhvjoTB1gaeujSJiz4cTB2jwHQhub-gFOaA6TrsCyaLJJpcxEKtZN_8m1cQ.; __Secure-3PSID=wQf5nBIQHQgbhvjoTB1gaeujSJiz4cTB2jwHQhub-gFOaA6Tpt5sV9o51FDB5usINboDBg.; HSID=ADdHimb0S8KX5VA62; SSID=AAuv3LLMZF850AAKk; APISID=2UlBRkYXAMfU59We/ANUtKu7-uI6k1RETo; SAPISID=FElk3eVC1mWfSpjj/A8NIR_9Y56BNGWTJD; __Secure-HSID=ADdHimb0S8KX5VA62; __Secure-SSID=AAuv3LLMZF850AAKk; __Secure-APISID=2UlBRkYXAMfU59We/ANUtKu7-uI6k1RETo; __Secure-3PAPISID=FElk3eVC1mWfSpjj/A8NIR_9Y56BNGWTJD; SEARCH_SAMESITE=CgQIyY8B; OTZ=5425784_44_48_120960_44_365700; __Secure-3PSIDCC=AJi4QfHgs2cw4n-6ovJe8PFt3yMvai3kZNLVjh3WctgCx2SJWh3MYdPbLZwe3oujCwf8wnZhzw; NID=203=EjCymI41NeCGQSZCAHWG9Pm3imjOvH_CK5-CwrmWQMbTBS8uGEZkfNfWJvf6NZMwa5XKyQVEVYuzT-uaE1E4CcOHlVW8KXK46l-TkX0Geh-Gj_cx3CL7W_ZbZc60071ruSGOgoQ24HvqkqYfybqoPNQJIzjCwk7K8MuBKNUXDxmU5WjuOhncWyY3BWx90MLabbSh4wN9wR55uCJatNeucmAYTchOEmuciLfJkwK6hwNnmKiJ2SpExGXyFV_fZsVA-1in5cNUw4jOAt1Upf35fS2Hqa9vXlXV6moe1FA; DV=s1Ou90m4Um9M0CFWiY5-nC2G70qBG5dw4P5MyRCtAwAAANCQSC0iEfN6cgAAAASD9CEe0G-oIQAAAA; 1P_JAR=2020-4-26-20; SIDCC=AJi4QfHfPkSFjmQ5aN7oQNnaf0aXacUWTCC4M1q6370BC2dT9QKHqfVC1RFXBUhHouCbHIwFwxU',
'referer': 'https://www.google.com/',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
'x-client-data': 'CIS2yQEIo7bJAQjBtskBCKmdygEI0K/KAQi8sMoBCO21ygEIjrrKAQjLx8oBGLu6ygE='
}
browser.get('https://www.google.com/')
search=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME,'q')))
search.send_keys('recaptcha demo')
search.send_keys(Keys.ENTER)
for x in browser.find_elements_by_tag_name('a'):
    if x.get_attribute('href')=='https://www.google.com/recaptcha/api2/demo': #change the URL to the targeted site
        x.click()        #redirection to reCAPTCHA website
        break

frames=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'iframe')))
for f in frames:
    try:
        if f.get_attribute('name')[0]=='a':
            frame=f
            break
    except: pass
browser.switch_to.frame(frame)
recaptcha=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID,'recaptcha-anchor')))
ActionChains(browser).move_to_element(recaptcha).perform()
recaptcha.click()       #redirection to the photo selection
browser.switch_to.default_content()
frames2=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'iframe')))
for f in frames2:
    try:
        if f.get_attribute('name')[0]=='c':
            frame2=f
            break
    except: pass
browser.switch_to.frame(frame2)
WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID,'recaptcha-audio-button'))).click()   #redirection to audio
browser.switch_to.default_content()
frames3=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'iframe')))
for f in frames3:
    try:
        if f.get_attribute('name')[0]=='c':
            frame3=f
            break
    except: pass
browser.switch_to.frame(frame3)
audio()
#WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,'recaptcha-demo-submit'))).click()
input()