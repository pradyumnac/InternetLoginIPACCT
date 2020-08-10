import os
import logging

import requests
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(filename='run.log',filemode='a', format = '%(name)s - %(asctime)s - %(message)s', level= logging.INFO)

url = "http://10.254.254.71/0/up/"
logged_in_str = "Your Internet connection is configured properly."
login_params = {'login': 'Login', 'user':os.environ.get('internet_uname'), "pass":os.environ.get('internet_passwd') }
logout_params = {'logout': 'Click here to logout'}


def check_logged_in():
	r = requests.get(url)
	return r.status_code==200 and logged_in_str in r.text


def logout():
	r = requests.post(url, data = logout_params)
	assert r.status_code==200 and check_logged_in() is False


def login():
	r = requests.post(url, data = login_params)
	assert r.status_code==200 and check_logged_in() is True

if __name__=="__main__":
	# logout()
    if not check_logged_in():
        logging.info("logging in ..")
        login()
        if not check_logged_in():
            logging.error(" Login Failed!")
        else:
            logging.info("Logging Success!")
