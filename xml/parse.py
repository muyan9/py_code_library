#!/usr/bin/python

# parsexml.py                                           
                                                        
import xml.parsers.expat                                
import xml.dom
level = 0                                               



def start_element(name, attrs):                         
    global level                                        
    print '  '*level, 'Start element:', name, attrs     
    level = level + 1                                   
                                                        
def end_element(name):                                  
    global level                                        
    level = level - 1                                   
    print '  '*level, 'End element:', name              
                                                        
def char_data(data):                                    
    if(data == '\n'):                                   
        return                                          
    if(data.isspace()):                                 
        return                                          
    global level                                        
    print '  '*level, 'Character data:', data           

p = xml.parsers.expat.ParserCreate()                    

p.StartElementHandler = start_element                   
p.EndElementHandler = end_element                       
p.CharacterDataHandler = char_data                      
p.returns_unicode = False                               

f = file('t.xml')
p.ParseFile(f)
f.close()
