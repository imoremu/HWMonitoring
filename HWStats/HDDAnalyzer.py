'''
Created on 6 de nov. de 2015

@author: imoreno
'''

class HDDAnalyzer(object):
         
    initialData = {}
    finalData = {}
    
    devStr = "dev" 
    readsStr = "reads"
    writeStr = "writes"    
    msReading = 'ms_reading'
    
    columns_disk = ['m', 'mm', devStr, readsStr, 'rd_mrg', 'rd_sectors',
                    msReading, writeStr, 'wr_mrg', 'wr_sectors',
                    'ms_writing', 'cur_ios', 'ms_doing_io', 'ms_weighted']

    columns_partition = ['m', 'mm', 'dev', 'reads', 'rd_sectors', 'writes', 'wr_sectors']

    '''
    Constructor
    '''
    def __init__(self, dev, initFile, finalFile):    
        self.initialData = self.parseFile(dev, initFile)
        self.finalData = self.parseFile(dev, finalFile)
       

    '''
    Parse diskstats files.
    
    '''
    def parseFile(self, dev, file):    
                
        lines = open(file, 'r').readlines()
        for line in lines:
            if line == '': continue
            
            split = line.split()
            
            if len(split) == len(self.columns_disk):
                columns = self.columns_disk
            elif len(split) == len(self.columns_partition):
                columns = self.columns_partition
            else:
                # No match
                continue
    
            data = dict(zip(columns, split))
            
            if dev != None and dev != data[self.devStr]:
                continue
            
            for key in data:
                if key != self.devStr:
                    data[key] = int(data[key])
            break      
                        
        return data    
        
    
    
    def getAccessResponseTime(self):
        
        readsNumber = self.finalData[self.readsStr] - self.initialData[self.readsStr] 
        timeReading = self.finalData[self.msReading] - self.initialData[self.msReading]
        
        result = -1;
        
        if (timeReading):
            result = readsNumber / timeReading;
        
        return result
                
        
