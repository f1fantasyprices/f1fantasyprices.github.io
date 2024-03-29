
from script.modules.xpaths import get_xpaths
from script.modules.helpers import *
import os


import time



def get_prices(webdriver, credentials):

    wdir = os.path.dirname(os.path.abspath(__file__))
    webdriver.set_window_size(1920, 1080)
    xpaths = get_xpaths()
    ## Load account page

    ### Enter account details
    zoom_out(webdriver,5)
    element_load(webdriver, xpaths['sign_in_btn'], 10, "css")
    webdriver.find_element_by_class_name(xpaths['username']).send_keys(credentials['username'])
    webdriver.find_element_by_class_name(xpaths['password']).send_keys(credentials['password'])
    webdriver.find_element_by_css_selector(xpaths['sign_in_btn']).click()


    element_load(webdriver, xpaths["manage"], 10, "xpath")
    time.sleep(5)
    webdriver.find_element_by_xpath(xpaths['manage']).click()

    try:
        element_load(webdriver, xpaths['accept_cookie'], 10, "xpaths")
        webdriver.find_element_by_xpath(xpaths['accept_cookie']).click()
    except:
        print("no cookie accept needed")


    element_load(webdriver, xpaths["next_1"], 10, "xpath")
    click_by_text(webdriver, 'div', 'Next')
    element_load(webdriver, xpaths["next_1"], 10, "xpath")
    click_by_text(webdriver, 'div', 'Next')
    element_load(webdriver, xpaths["done"], 10, "xpath")
    webdriver.find_element_by_xpath(xpaths['done']).click()

    time.sleep(2)
    element_load(webdriver, xpaths["expose_list"], 10, "xpath")
    webdriver.find_element_by_xpath(xpaths['expose_list']).click()
    #click_by_text(webdriver, 'div', 'Done')



    # Zoom out the page
    zoom_out(webdriver, 5)

    click_by_text(webdriver, 'span', 'DR')

    element = webdriver.find_element_by_class_name(xpaths['driver_card'])
    html = element.get_attribute('innerHTML')
    driver_df = get_drivers(html)

    update_driver_prices(driver_df, wdir + '/data/resources/driver_prices.xlsx')


    click_by_text(webdriver, 'span', 'CR')
    time.sleep(3)
    element = webdriver.find_element_by_class_name(xpaths['driver_card'])
    html = element.get_attribute('innerHTML')
    constructor_df = get_drivers(html)
    constructor_df.to_excel(wdir + "/data/resources/constructor_df.xlsx", index=False)

    update_driver_prices(constructor_df, wdir + '/data/resources/constructor_prices.xlsx')



