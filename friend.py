from selenium import webdriver
import time
from bs4 import BeautifulSoup

 
webpage = webdriver.Chrome()

webpage.get("https://facebook.com")

email = webpage.find_element_by_id("email")
email.send_keys("rushabhfight@gmail.com")

password = webpage.find_element_by_id("pass")
password.send_keys(")(*&^%$#@!!@#$%^&*()")

login = webpage.find_element_by_id("u_0_b")
login.click()

time.sleep(20)

pro_btn = webpage.find_element_by_xpath('//a[@class="_2s25 _606w"]')
pro_btn.click()

time.sleep(20)

friend_btn = webpage.find_element_by_xpath('//span[@class="_gs6"]')
friend_btn.click()

while True:
	webpage.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	webpage.execute_script('window.scrollTo(0,0);')
	try:
		end = webpage.find_element_by_xpath('//h3[contains(text(),"More about you")]')
		break
	except:
		continue

page_code = webpage.page_source
soup = BeautifulSoup(page_code, 'html.parser')
friend_list = soup.find('div',{'class':'_3i9'})

friend_data = []
for i in friend_list.findAll('a'):
	friend_data.append(i.text)

flist = []
for name in friend_data:
	if name == 'FriendFriends':
		continue
	if 'friends' in name:
		continue
	if name == '':
		continue
	else:
		flist.append(name)
print(flist)