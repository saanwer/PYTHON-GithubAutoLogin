import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Github Auto Login
#Coded by | WarLord
#https://github.com/saanwer
def getID(url):
	pUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(pUrl.query)['id'][0]

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("email", help="Github email")
	parser.add_argument("password", help="Github password")
	args = parser.parse_args()

	browser = webdriver.Firefox()
	browser.get("https://github.com/login")

	emailElement = browser.find_element_by_id("login_field")
	emailElement.send_keys(args.email)
	passElement = browser.find_element_by_id("password")
	passElement.send_keys(args.password)
	passElement.submit()

	os.system('cls')#os.system('clear') if Linux
	print "[+] Auto login success!"
	browser.close()

if __name__ == "__main__":
	Main()
