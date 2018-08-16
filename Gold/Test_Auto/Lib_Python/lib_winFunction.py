# -*- coding: cp1252 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.libraries.BuiltIn import BuiltIn
import time
from ctypes import * 
import win32gui
import win32com.client


"""
    Function compatible with Windows server
"""
class lib_winFunction(object):
    #send login psswd in popup
    def login_popup(self,login,pwd):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()

        driver.implicitly_wait(5)
        shell = win32com.client.Dispatch("WScript.Shell")           
        time.sleep(5)
        shell.SendKeys(login,0)
        shell.SendKeys("{TAB}",0)
        shell.SendKeys(pwd,0)
        shell.SendKeys("{TAB}",0)
        shell.SendKeys("{ENTER}",0)
        print "No alert exists"

    def open_poppupfichier(self):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        
        if (EC.alert_is_present()) : 
            driver.implicitly_wait(5)
            shell = win32com.client.Dispatch("WScript.Shell")           
            time.sleep(5)
            shell.SendKeys("{TAB}",0)
            shell.SendKeys("{ENTER}",0)
            print "fin test"
        else :
            print "No alert exists"

    def save_poppup(self):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        
        if (EC.alert_is_present()) : 
            driver.implicitly_wait(5)
            shell = win32com.client.Dispatch("WScript.Shell")           
            time.sleep(5)
            shell.SendKeys("{ENTER}",0)
            shell.SendKeys("{ENTER}",0)
            print "fin test"
        else :
            print "No alert exists"

    def up(self,path):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        
        if (EC.alert_is_present()) : 
            driver.implicitly_wait(5)
            shell = win32com.client.Dispatch("WScript.Shell")           
            time.sleep(2)
            shell.SendKeys(path,0)
            time.sleep(2)
            shell.SendKeys("{ENTER}",0)
            print "upload done"
        else :
            print "No alert exists"
            
    def down(self):
        #get browser opened
        newLib = BuiltIn().get_library_instance('Selenium2Library')
        driver = newLib._current_browser()
        
        if (EC.alert_is_present()) : 
            driver.implicitly_wait(5)
            shell = win32com.client.Dispatch("WScript.Shell")            
            time.sleep(2)
            shell.SendKeys("{DOWN}",0)          
            time.sleep(2)
            shell.SendKeys("{ENTER}",0)
            print "download done"
        else :
            print "No alert exists"

    def simulateKeyboard(self,toucheClavier):
        #get browser opened
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys(toucheClavier,0)
        time.sleep(0.2)
 