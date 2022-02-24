from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time
import json
import requests
import datetime
import urllib
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from Consultas import Empresa
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import os
import sys
from datetime import date
from selenium.webdriver.firefox.options import Options
from datetime import datetime, timedelta
from threading import Timer


x=datetime.today()
y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()



options = Options()
options.headless = True
options.add_argument('--force-device-scale-factor=1.5')
browser = webdriver.Firefox()



def getandsendhomework():
    browser.get('https://www.santillanaconnect.com/Account/Login/?wtrealm=http%3a%2f%2flms30.santillanacompartir.com%2flogin%2fmoderna%2f&wreply=https%3a%2f%2flms30.santillanacompartir.com%2flogin%2fsso%2floginconnect')
    

    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")

    username.send_keys("br.cmpm.gustavo.souza")
    password.send_keys("miojo001")


    browser.find_element_by_id("submit").click()
    # form = browser.find_element_by_name("loginForm")

    # form.submit()
    time.sleep(2)
    browser.find_element_by_id("accessSubmit").click()
    time.sleep(5)
    browser.find_element_by_class_name("class-card-kids__title--text").click()
    browser.find_element_by_link_text("Atividades").click()
    time.sleep(2)
    browser.save_screenshot("LC_Hj.png")


    time.sleep(2)
    browser.get("https://discord.com/channels/935570894317826088/935604350162714684")

    browser.find_element_by_name("email").send_keys("gus.moura1909@gmail.com")
    browser.find_element_by_name("password").send_keys("madre123456789")
    browser.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)
    browser.find_element_by_class_name("file-input").send_keys(os.getcwd()+"\LC_Hj.png")
    # time.sleep(1)
    # browser.find_element_by_class_name("uploadInput-YH_iku").click()
    time.sleep(2)
    # pyautogui.write('C:\\Users\\user\\Desktop\\project_lc\\LC_Hj.png') 
    # time.sleep(1)
    # pyautogui.press('return')
    time.sleep(2)
    pyautogui.press('return')
    pyautogui.press('return')
    print("Lc de casa enviada!")


t = Timer(secs, getandsendhomework)
t.start()