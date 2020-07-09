from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time

url = "https://www.youtube.com/watch?v=aA-s0KoeM68"
#영일남 디아더스 2부

driver = wd.Chrome(executable_path="C:\\Python\\youtubeComments\\chromedriver.exe")
driver.get(url)

last_page_heigth = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_heigth:
        break;
    last_page_heigth = new_page_height

html_source = driver.page_source

driver.close()

soup = BeautifulSoup(html_source, 'html.parser')
youtube_user_IDs = soup.select('div#header-author > a > span')
youtube_comments = soup.select('yt-formatted-string#content-text')

str_youtube_userIDs = []
str_youtube_comments = []

for i in range(len(youtube_user_IDs)):
    str_tmp = str(youtube_user_IDs[i].text)
    str_tmp = str_tmp.replace('\n','')
    str_tmp = str_tmp.replace('\t','')
    str_tmp = str_tmp.replace('                ','')
    str_youtube_userIDs.append(str_tmp)

    str_tmp = str(youtube_comments[i].text)
    str_tmp = str_tmp.replace('\n','')
    str_tmp = str_tmp.replace('\t','')
    str_tmp = str_tmp.replace('                ','')
    str_youtube_comments.append(str_tmp)

for i in range(len(str_youtube_userIDs)):
    print(str_youtube_userIDs[i]+"\n"+str_youtube_comments[i]+"\n")


