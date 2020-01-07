# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:15:13 2019

@author: 86158
"""
import time
from selenium import webdriver


from bs4 import BeautifulSoup
#browser = webdriver.PhantomJS("E:\\phantomjs\\bin\\phantomjs.exe")

#browser = webdriver.PhantomJS(r"E:\phantomjs\bin\phantomjs.exe")

browser = webdriver.Chrome(r"E:\chrome\chromedriver.exe")
browser.get("http://www.taobao.com")

page_sour=browser.page_source
soup=BeautifulSoup(page_sour,'lxml')

soup.find(id="J_SiteNavBdL")
soup.find(name="div",class_="J_SiteNavBdL")

soup.p
browser.find_element_by_name('p')

input_p=browser.find_element_by_id("J_SiteNavBdL")
input_t=browser.find_element_by_css_selector('#J_SiteNavBdL')
        
input_x=browser.find_element_by_xpath('//*[@id="J_SiteNavBdL"]')
print (input_p.text)
print (soup_d.text)





