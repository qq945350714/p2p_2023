import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from app import base_dir
from script.all_tender import mytender
from script.approve import approve
from script.login import login
from script.tender import tender
from script.trust import trust




suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))
suite.addTest(unittest.makeSuite(approve))
suite.addTest(unittest.makeSuite(trust))
suite.addTest(unittest.makeSuite(tender))
suite.addTest(unittest.makeSuite(mytender))


report_file = base_dir + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(file=report_file,mode="wb") as f:
    runner = HTMLTestRunner(f, title="p2p测试报告")
    runner.run(suite)
