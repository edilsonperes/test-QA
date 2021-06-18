from selenium import webdriver

def before_all(context):
    context.web = webdriver.Firefox()

def after_all(context):
    context.web.quit()