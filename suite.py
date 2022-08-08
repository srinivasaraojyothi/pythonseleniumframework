import stepdefs.test_unit_example
import stepdefs.test_unit_example_1
import unittest
import HtmlTestRunner

#from stepdefs.test_unit_example_1 import SampleTestCase_2

test_suite = unittest.TestSuite()
test_suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(stepdefs.test_unit_example.SampleCase),unittest.defaultTestLoader.loadTestsFromTestCase(stepdefs.test_unit_example_1.SampleCase_2),])
testResult = unittest.TestResult()
test_suite.run(testResult)
#testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports",combine_reports=True)
#testRunner.run(test_suite)

    
if __name__ == '__main__':
        unittest.main()