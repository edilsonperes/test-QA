from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import randint

@given(u'User access "mytime" page')
def step_impl(context):
    context.web.get("https://www.mytime.com/consumers")
    sleep(1)
    context.web.find_element_by_css_selector("#accept-cookies-and-close-button").click()

@given(u'Searches for a service in a city')
def step_impl(context):
    context.web.find_element_by_css_selector(".search-container > div:nth-child(1) > input:nth-child(2)").send_keys('haircut')
    context.web.find_element_by_css_selector("div.search-bar-item:nth-child(2) > input:nth-child(2)").clear()
    context.web.find_element_by_css_selector("div.search-bar-item:nth-child(2) > input:nth-child(2)").send_keys('San Francisco, CA')
    context.web.find_element_by_css_selector(".flat-blue-btn").click()


@given(u'User is presented with at least 3 reasults')
def step_impl(context):
    sleep(5)
    context.res_list = context.web.find_element_by_id("results")
    context.res_items = context.res_list.find_elements_by_tag_name("li")
    assert len(context.res_items) >= 3, "Less than 3 results shown"

@when(u'User opens any business')
def step_impl(context):
    #context.res_items[randint(1, len(res_items))].click()
    context.res_items[4].click()


@when(u'Selects all services in the services filter from the left panel')
def step_impl(context):
    sleep(5)
    context.web.find_element_by_css_selector(".service > fieldset:nth-child(2) > label:nth-child(1) > span:nth-child(2)").click()


@when(u'Selects second staff in the staff filter from the left panel')
def step_impl(context):
    context.web.find_element_by_css_selector(".staff-member > fieldset:nth-child(2) > label:nth-child(3) > span:nth-child(2)").click()
    context.staff = context.web.find_element_by_css_selector(".staff-member > fieldset:nth-child(2) > label:nth-child(3) > span:nth-child(2)").text

@when(u'Clicks the button "Men`s Haircut" service')
def step_impl(context):
    context.service = context.web.find_element_by_css_selector("section.service-category:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h5:nth-child(1) > span:nth-child(1)").text
    context.price = context.web.find_element_by_css_selector("section.service-category:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
    context.web.find_element_by_css_selector("section.service-category:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)").click()


@when(u'Clicks "Select Time" in the add-on modal opened')
def step_impl(context):
    context.web.find_element_by_css_selector(".select-time-button").click()

@then(u'User is presented with a list of available time slots with at least 2 entries')
def step_impl(context):
    sleep(5)
    time_list = context.web.find_element_by_css_selector("div.panel:nth-child(3)")
    time_item = 1
    while True:
        try:
            time_list.find_element_by_css_selector("div.opentime-item:nth-child({})".format(time_item))
            time_item += 1
        except NoSuchElementException as exception:
            break
    assert time_item - 1 >= 2, "Less than 2 available times"


@then(u'Service displayed in the right side panel is the one selected before')
def step_impl(context):
    #context.service = "Women's hair cut"
    assert context.web.find_element_by_css_selector(".variation-name").text == context.service, "Service is different from selected before"


@then(u'Service price in the right side panel is the same as the one displayed before')
def step_impl(context):
    #context.price = "$100.00"
    assert context.web.find_element_by_css_selector(".variation-price > span:nth-child(1)").text == context.price, "Price is different from presented before"


@then(u'Staff selected is the staff chosen before')
def step_impl(context):
    #context.staff = "Master Yoda"
    assert context.web.find_element_by_id("react-select-4--value-item").text == context.staff, "Staff is different from selected before"
