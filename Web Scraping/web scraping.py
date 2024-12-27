import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:/Users/Student/Desktop/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://oxylabs.io/blog')
content = driver.page_source
driver.quit()

soup = BeautifulSoup(content, 'html.parser')

results = []
for element in soup.find_all(attrs={'class': 'oxy-uyso8s estdcpb2'}):
    name = element.find('p')
    if name and name.text not in results:
        results.append(name.text)

df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')
