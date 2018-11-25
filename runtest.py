# -*- coding: utf-8 -*-
"""
@author: zh
"""
import unittest
from datetime import datetime
from HTMLTestRunner import HTMLTestRunner

discover=unittest.defaultTestLoader.discover("./TestCase","[Tt]est*.py")

if __name__ == '__main__':
    now=datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    filename="./Report/%s_report.html"%now
    with open(filename,"wb") as f:
        runner=HTMLTestRunner(f,title="百度测试报告",description="用例")
        runner.run(discover)
