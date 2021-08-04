import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.google.com/search?q=bitcoin+price+usd&oq=bitcoin+price+usd&aqs=chrome.0.35i39j0i67j0i395l5j69i61.7034j1j7&sourceid=chrome&ie=UTF-8')
soup = BeautifulSoup(r.text,'html.parser')
print(soup)