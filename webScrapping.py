from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path=r"C:\Users\giljv\Downloads\chromedriver_win32\chromedriver.exe"

#Open in background
options = Options()
options.headless = True

service = Service(executable_path=path) 
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

titles = []
subtitles = []
links = []

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')
for container in containers:
  titles.append(container.find_element(by='xpath', value='./a/h2').text)
  subtitles.append(container.find_element(by='xpath', value='./a/p').text)
  links.append(container.find_element(by='xpath', value='./a').get_attribute("href"))

driver.quit()

my_dict = {'titles':titles, 'subtitles':subtitles, 'links':links}
my_df_news = pd.DataFrame(my_dict)

my_df_news.to_csv('News.csv')