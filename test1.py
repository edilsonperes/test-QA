from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import randint

driver = webdriver.Firefox()
driver.get("https://www.mytime.com/consumers")

sleep(1)

driver.find_element_by_css_selector("#accept-cookies-and-close-button").click()

#Digita a pesquisa e clica no botao pesquisar
driver.find_element_by_css_selector(".search-container > div:nth-child(1) > input:nth-child(2)").send_keys('haircut')
driver.find_element_by_css_selector("div.search-bar-item:nth-child(2) > input:nth-child(2)").clear()
driver.find_element_by_css_selector("div.search-bar-item:nth-child(2) > input:nth-child(2)").send_keys('San Francisco, CA')
driver.find_element_by_css_selector(".flat-blue-btn").click()

sleep(5)

#Conta os resultados, checka se ha mais que 3 e seleciona 1 deles aleatoreamente
res_list = driver.find_element_by_id("results")
res_items = res_list.find_elements_by_tag_name("li")
assert len(res_items) >= 3, "Less than 3 results shown"
#res_items[randint(1, len(res_items))].click()
res_items[4].click()

sleep(5)

#Seleciona all services, segundo membro da equipe e salva o nome do membro selecionado
driver.find_element_by_css_selector(".service > fieldset:nth-child(2) > label:nth-child(1) > span:nth-child(2)").click()
driver.find_element_by_css_selector(".staff-member > fieldset:nth-child(2) > label:nth-child(3) > span:nth-child(2)").click()
staff = driver.find_element_by_css_selector(".staff-member > fieldset:nth-child(2) > label:nth-child(3) > span:nth-child(2)").text

#Salva o nome do servico, preco e seleciona o servico
service = driver.find_element_by_css_selector("section.service-category:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h5:nth-child(1) > span:nth-child(1)").text
price = driver.find_element_by_css_selector("section.service-category:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
driver.find_element_by_css_selector("section.service-category:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)").click()
driver.find_element_by_css_selector(".select-time-button").click()

sleep(5)

time_list = driver.find_element_by_css_selector("div.panel:nth-child(3)")
time_item = 1
while True:
    try:
        time_list.find_element_by_css_selector("div.opentime-item:nth-child({})".format(time_item))
        time_item += 1
    except NoSuchElementException as exception:
        break
assert time_item - 1 >= 2, "Less than 2 available times"

#service = "Women's hair cut"
#price = "$100.00"
#staff = "Master Yoda"

assert driver.find_element_by_css_selector(".variation-name").text == service, "Service is different from selected before"
assert driver.find_element_by_css_selector(".variation-price > span:nth-child(1)").text == price, "Price is different from presented before"
assert driver.find_element_by_id("react-select-4--value-item").text == staff, "Staff is different from selected before"

sleep(3)

driver.close()