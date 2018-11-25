# -*- coding: utf-8 -*-
"""
@author: zh
"""
from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\lenovo\AppData\Local\Google\Chrome\Application\chromedriver.exe")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.get("http://www.baidu.com")
        time.sleep(2)
        self.driver.find_element_by_css_selector("#kw").send_keys("unittest")
        self.driver.find_element_by_css_selector("#su").click()

if __name__ == '__main__':
    testSuit=unittest.TestSuite()
    testSuit.addTest(TestBaidu("test_baidu_search"))

    with open("./report.html","wb") as f:
        runner=HTMLTestRunner(f,title="百度搜索测试报告",description="用例执行情况")
        runner.run(testSuit)