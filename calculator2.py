# coding: utf-8
from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/windows/system32/calc.exe"
    })

window = driver.find_element_by_class_name('ApplicationFrameWindow')
driver.find_element_by_id('num8Button').click()
#driver.quit()