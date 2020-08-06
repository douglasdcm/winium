# coding: utf-8
from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/windows/system32/calc.exe"
    })

window = driver.find_element_by_class_name('ApplicationFrameWindow')
#calculadora = window.find_element_by_class_name('Windows.UI.Core.CoreWindow')
#grupo = calculadora.find_element_by_class_name('LandmarkTarget')
#teclado = grupo.find_element_by_class_name('NamedContainerAutomationPeer')
driver.find_element_by_id('num8Button').click()

#view_menu_item = window.find_element_by_id('PaneRoot').find_element_by_name('MenuItemsHost')

#view_menu_item.click()
#view_menu_item.find_element_by_name('Scientific').click()

#view_menu_item.click()
#view_menu_item.find_element_by_name('History').click()

#window.find_element_by_name('Oito').click()
#window.find_element_by_id('93').click()
#window.find_element_by_id('134').click()
#window.find_element_by_id('97').click()
#window.find_element_by_id('138').click()
#window.find_element_by_id('121').click()

driver.close()