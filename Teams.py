from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("https://intranet.bomjesus.br/")

usuario = driver.find_element_by_xpath("//input[@id='txtUsuario']")
usuario.click()

usuario.send_keys("laurafaria")

senha = driver.find_element_by_xpath("//input[@type='password']")
senha.click()
senha.send_keys("Laura2108@")

senha.send_keys(Keys.ENTER)

time.sleep(1.0)

email = driver.find_element_by_xpath("//a[@class='icone i_perfil_email']")
email.click()
time.sleep(3.0)
abas = driver.window_handles
driver.switch_to_window(abas[1])

time.sleep(3.0)
gmail = driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")
gmail.click()