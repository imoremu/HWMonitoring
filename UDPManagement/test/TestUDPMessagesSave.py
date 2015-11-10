'''
Created on 10 de nov. de 2015

@author: imoreno
'''
import unittest
import socket
import UDPManagement


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testUDPMessageSave(self):
        
        # Send a message in the proper port
        MCAST_GRP = '224.1.1.1'
        MCAST_PORT = 5007
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        
        sock.sendto("Message Sent", (MCAST_GRP, MCAST_PORT))
    
        # Save message 
        UDPManagement.UDPManagement udp
        UDPManagement.UDPManagement.saveData(MCAST_GRP, MCAST_PORT);
        
        # Get message from database
        
    
        # Assert that message is included in database with metadata: message type, version, payload         
        
        self.fail("Not implemented yet")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testUDPMessageSave']
    unittest.main()