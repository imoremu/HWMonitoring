'''
Created on 6 de nov. de 2015

@author: imoreno
'''
import configparser
import unittest

from HWStats.HDDAnalyzer import HDDAnalyzer


class Test(unittest.TestCase):

    testInitialFile = "files/initial_HD_stats.txt"
    testFinalFile = "files/final_HD_stats.txt"
    
    # Properties file for testing.

    propertiesFile = "files/HW_stats_test.properties"
    
    settings = configparser.ConfigParser()
    settings.read(propertiesFile)
    
    def testHDDAccessResponseTime(self):
                                  
        analyzer = HDDAnalyzer(self.settings.get('TEST_PARAMETERS', 'dev'), self.testInitialFile, self.testFinalFile)
    
        accessResponseTime = analyzer.getAccessResponseTime()        
        expectedValue = int(self.settings.get('TEST_RESULTS', 'accessTimeTest'))
                                                       
        self.assertEqual(accessResponseTime, 10, "Access response time: {current} - Should be: {expected}".format(current=accessResponseTime, expected=expectedValue))

    
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
