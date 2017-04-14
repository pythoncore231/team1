'''
Created on Apr 13, 2017

@author: vodachuk
'''

class Base(object):
    '''
    id save() read()
    '''


    def __init__(self, id = 0):
        '''
        Constructor
        '''
        self.id = 0
    
    def to_unicode(self):
        return unicode(self.id)    
    
    def save(self):
        pass
    def read(self):
        pass